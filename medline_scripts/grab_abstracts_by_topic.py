#!/usr/bin/python
#$ -S /usr/bin/python

'''
This script examines a file or a list of files, and prints all
of the abstracts to a file.
'''

import xml.etree.ElementTree as et
import os
import operator
import copy
import sys

def processFile(filePath, topic):

  tree = et.parse(filePath)
  root = tree.getroot()

  # For each abstract/citation...
  for citation in root.iter('MedlineCitation'):

    # If this article has a mesh list...
    for descriptor in citation.findall('.//DescriptorName'):

      # And there is a topic match...
      if descriptor.text == topic:

        # Grab each abstract
        for abstractText in citation.findall('.//AbstractText'):
          print '<Abstract>'
          print abstractText.text
          print '</Abstract>'

        break

def main():

  if len(sys.argv) != 3:
    print 'Invalid arguments'
    print 'Usage: `python grab_abstracts_by_topic.py [file1 file2] [your_topic]`'
    sys.exit()

  files = sys.argv[1].split()
  topic = sys.argv[2]

  print '<Abstracts>'
  print '<Topic>' + topic + '</Topic>'

  for f in files:
    processFile(f, topic)

  print '</Abstracts>'

if __name__ == "__main__":
  main()