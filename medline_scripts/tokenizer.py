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
  return count >= 5

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

def processFile(tokenDict, filename):

  filePath = folderPath + '/' + filename

  xml = ''
  with open(filePath) as f:

    # Honestly, having to do this is just stupid on my part...
    # the [topic].xml files are not perfectly valid xml, so you
    # have to 'fix' them before parsing.
    xml = f.read()
    xml = re.sub(r'(<\?xml[^>]+\?>)', '', xml)
    xml = '<?xml version=\'1.0\' encoding=\'utf8\'?>' + xml
    xml = re.sub(r'(<\?xml[^>]+\?>)', r'\1\n<root>', xml) + '</root>'

  parser = et.XMLParser(encoding='utf-8')
  root = et.fromstring(xml, parser=parser)

  for abstractTextElement in root.findall('.//AbstractText'):
    abstractText = abstractTextElement.text
    abstractTokens = nltk.word_tokenize(abstractText)

    for tok in abstractTokens:
      if tok in tokenDict:
        tokenDict[tok] += 1
      else:
        tokenDict[tok] = 1

  topicDict[topic] = tokenDict

folderPath = '/Users/Zack/Developer/maple/medline_scripts/scripts_output/abstracts_by_topic'
topicDict = dict()

tokensX = []
typesY = []

for f in os.listdir(folderPath):
  topic = f[:-4]
  tokenDict = dict()

  processFile(tokenDict, f)
  topicDict[topic] = tokenDict

  tokens = countTokens(tokenDict, countPredicate)
  types = countTypes(tokenDict, countPredicate);

  print tokens, types

  tokensX.append(tokens)
  typesY.append(types)

plt.scatter(tokensX, typesY)
plt.xlabel('tokens')
plt.ylabel('types')
plt.grid(True)
plt.savefig('types_vs_tokens_per_topic.png')
plt.show()



