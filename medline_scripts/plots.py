#!/usr/bin/python
#$ -S /usr/bin/python

'''
This script does the following:
Calculates: the total number of abstracts, types and tokens
Plots types vs. tokens (essentially a line chart, with the x-axis being
number of tokens processed, and the y-axis being number of types identified)
An identical plot as the one mentioned above, but this time ignoring
any token/type with <= 5 occurrences
A histogram of counts of tokens (i.e. take the top 100-1000 tokens, and
make a histogram of their counts)
'''

import lxml.etree as et
import os
import re
import operator
import nltk
import matplotlib.pyplot as plt
import string
import numpy as np
import sys

def countPredicate(count):
  return count >= 0

def countTokens(tokenDict, predicate):
  total = 0
  for tok, count in tokenDict.iteritems():
    if predicate(count):
      total += count

  return total

def countTypes(tokenDict, predicate):
  total = 0
  for tok, count in tokenDict.iteritems():
    if predicate(count):
      total += 1

  return total

'''
# this method counts the number of abstracts
# counts the number of types and tokens at each iteration
# and returns both of them as lists
'''
def processFile(filePath):

  tokenDict = dict()
  parser = et.XMLParser(encoding='utf-8', recover=True)
  root = et.parse(filePath, parser)
  count = 0
  indexTokens = 0
  indexTypes = 0
  numTokens = [0]
  numTypes = [0]

  for abstractTextElement in root.findall('.//File//Abstract'):
    abstractText = abstractTextElement.text
    count += 1

    # remove any punctuation before tokenizing.
    abstractText = abstractText.encode('utf-8').translate(None, string.punctuation)
    abstractTokens = nltk.word_tokenize(abstractText)

    for tok in abstractTokens:
      # token count always increases
      numTokens.append(numTokens[indexTokens] + 1)
      indexTokens+=1

      if tok in tokenDict:
        tokenDict[tok] += 1
        # if this word has occurred before, number of types stays the same
        numTypes.append(numTypes[indexTypes])
      else:
        tokenDict[tok] = 1
        # new word so number of types increases
        numTypes.append(numTypes[indexTypes] + 1)
      indexTypes += 1

  return (tokenDict, numTokens, numTypes, count)

'''
# This methods process the file again assuming it has already been processed
by a countDictionary. Using that, it ignores tokens and types that have appeared
less than or equal to count times
'''
def processFileIgnoring(filePath, countDict, count):

  tokenDict = dict()
  parser = et.XMLParser(encoding='utf-8', recover=True)
  root = et.parse(filePath, parser)
  root = et.parse(filePath)
  indexTokens = 0
  indexTypes = 0
  numTokens = [0]
  numTypes = [0]

  for abstractTextElement in root.findall('.//File//Abstract'):
    abstractText = abstractTextElement.text

    # remove any punctuation before tokenizing.
    abstractText = abstractText.encode('utf-8').translate(None, string.punctuation)

    abstractTokens = nltk.word_tokenize(abstractText)

    for tok in abstractTokens:
      if (countDict[tok] > count) :
        numTokens.append(numTokens[indexTokens] + 1)
        indexTokens+=1

        if tok in tokenDict:
          tokenDict[tok] += 1
          numTypes.append(numTypes[indexTypes])
        else:
          tokenDict[tok] = 1
          numTypes.append(numTypes[indexTypes] + 1)
        indexTypes += 1

  return (numTokens, numTypes)




def main():

  fileName = sys.argv[1]
  filePath = '/Users/Zack/Developer/maple/medline_scripts/scripts_output/abstracts_by_topic/' + fileName + '.xml'
  plotsPath = 'plots_output/' + fileName + '/'
  tokensX = []
  typesY = []

  # Process the file and calculate number of abstracts, tokens and types
  tokenDict, numTokens, numTypes, abstracts = processFile(filePath)
  tokens = countTokens(tokenDict, countPredicate)
  types = countTypes(tokenDict, countPredicate);

  # 1st plot
  tokensX = numTokens
  typesY = numTypes
  plt.plot(tokensX, typesY)
  plt.xlabel('tokens')
  plt.ylabel('types')
  plt.grid(True)
  plt.savefig(plotsPath + 'types_vs_tokens.png')
  plt.clf()

  # 2nd plot
  count = 5
  numTokens, numTypes = processFileIgnoring(filePath, tokenDict, count)
  tokensX = numTokens
  typesY = numTypes

  plt.plot(tokensX, typesY)
  plt.xlabel('tokens')
  plt.ylabel('types')
  plt.grid(True)
  plt.savefig(plotsPath + 'types_vs_tokens_ignoring_counts.png')
  plt.clf()

  # 3rd plot
  # sort the dictionary by values(counts) in decreasing order
  sorted_dict = sorted(tokenDict.items(), key=operator.itemgetter(1), reverse=True)

  # truncate the sorted_dictionary, can set this to 100 or 1000
  limit = 100
  truncated_dict = sorted_dict [0:limit]

  # iterate over the top values of the dictionaries to get their counts
  barY = []
  for token in truncated_dict:
    barY.append(tokenDict[token[0]])

  index = np.arange(100) + 1
  bar_width = 0.60
  opacity = 0.4
  error_config = {'ecolor': '0.3'}

  # plot stuff
  plt.bar(index, barY, bar_width, alpha=opacity, color='b', error_kw=error_config)
  plt.xlabel('Top 100 Tokens')
  plt.ylabel('Count')
  plt.grid(True)
  plt.savefig(plotsPath + 'top_100_tokens.png')

if __name__ == "__main__":
  main()
