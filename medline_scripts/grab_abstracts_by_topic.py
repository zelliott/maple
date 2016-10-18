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

        print '<Abstract>'

        # Grab each abstract
        for abstractText in citation.findall('.//AbstractText'):
          text = et.tostring(abstractText, encoding='utf8', method='text')
          text = text.replace('&', '&amp;')
          text = text.replace('<', '&lt;')
          text = text.replace('>', '&gt;')

          if text:
            print text

        print '</Abstract>'
        break

def main():

  if len(sys.argv) != 2:
    print 'Invalid arguments'
    print 'Usage: `[list of files] | python grab_abstracts_by_topic.py [your_topic]`'
    sys.exit()

  topic = sys.argv[1]

  print '<FilesAbstracts>'
  print '<Topic>' + topic + '</Topic>'

  for f in sys.stdin:
    print '<File>'
    processFile(f[:-1], topic)
    print '</File>'

  print '</FilesAbstracts>'

if __name__ == "__main__":
  main()