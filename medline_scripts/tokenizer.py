#!/usr/bin/python
#$ -S /usr/bin/python

'''
This script does a couple of different things:
- For each [topic].xml file
  - Grab all of the words from each abstract
  - Tokenizes these words using nltk
  - Count tokens & types
- Plots the tokens vs types for each topic
'''

import xml.etree.ElementTree as et
import os
import re
import nltk
import matplotlib.pyplot as plt

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

def processFile(filePath):

  tokenDict = dict()
  # parser = et.XMLParser(encoding='utf-8')
  root = et.parse(filePath)

  for abstractTextElement in root.findall('.//Abstract'):
    abstractText = abstractTextElement.text
    abstractTokens = nltk.word_tokenize(abstractText)

    for tok in abstractTokens:
      if tok in tokenDict:
        tokenDict[tok] += 1
      else:
        tokenDict[tok] = 1

  return tokenDict

def main():
  folderPath = '/Users/Zack/Developer/maple/medline_scripts/test_xml/test_tokenizer'
  topicDict = dict()
  tokensX = []
  typesY = []

  for f in os.listdir(folderPath):
    topic = f[:-4]
    tokenDict = processFile(folderPath + '/' + f)
    topicDict[topic] = tokenDict

    tokens = countTokens(tokenDict, countPredicate)
    types = countTypes(tokenDict, countPredicate);
    tokensX.append(tokens)
    typesY.append(types)

  plt.scatter(tokensX, typesY)
  plt.xlabel('tokens')
  plt.ylabel('types')
  plt.grid(True)
  plt.savefig('types_vs_tokens_per_topic.png')
  plt.show()

if __name__ == "__main__":
  main()