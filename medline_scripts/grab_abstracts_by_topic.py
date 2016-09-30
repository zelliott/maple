#!/usr/bin/python
#$ -S /usr/bin/python

# This script examines either a single file or a dir of files
# and counts (1) the number of medline citations (i.e. abstracts)
# and (2) the number of citations with mesh headings specified.

import xml.etree.ElementTree as et
import os
import operator
import copy
import sys

folderPath = '/nlp/data/corpora/medline_data/xml_files'
# folderPath = '/home1/z/zelliott/developer/cis400/test_xml'
# folderPath = '/Users/Zack/Developer/maple/medline_scripts/test_xml/'

if len(sys.argv) != 2:
  print "Specify a topic: `python grab_abstracts_by_topic.py [your topic]`"
  sys.exit()

count = 0
topic = sys.argv[1]

def processFile(filename):
  global count
  global topic

  tree = et.parse(folderPath + '/' + filename)
  root = tree.getroot()

  # Count each abstract/citation
  for citation in root.iter('MedlineCitation'):

    # If this article has a mesh list...
    for descriptor in citation.findall('.//DescriptorName'):
      if descriptor.text == topic:
        count += 1
        print et.tostring(citation, encoding='utf8', method='xml')
        break

print topic

# for f in os.listdir(folderPath):
processFile('medline15n0778.xml')
# processFile('test_grab_abstracts_by_topic.xml')

print count