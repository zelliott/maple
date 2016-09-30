#!/usr/bin/python
#$ -S /usr/bin/python

# This script examines either a single file or a directory of files
# (depending upon what is commented out in this script) and returns
# a list of descriptors sorted by their frequency in the file (i.e.
# the number of occurences, or count).

import xml.etree.ElementTree as et
import os
import operator

folderPath = '/nlp/data/corpora/medline_data/xml_files'
# folderPath = '/home1/z/zelliott/developer/cis400/test_xml'
countByDescriptor = dict()

def processFile(filename):
  tree = et.parse(folderPath + '/' + filename)
  root = tree.getroot()

  for descriptor in root.findall('.//DescriptorName'):
    if descriptor.text in countByDescriptor:
      countByDescriptor[descriptor.text] += 1
    else:
      countByDescriptor[descriptor.text] = 1

# for f in os.listdir(folderPath):
processFile('medline15n0777.xml')
# processFile('test_decriptors_by_popularity_a.xml')

sortedDescriptors = sorted(
  countByDescriptor,
  key=countByDescriptor.__getitem__,
  reverse=True)

for d in sortedDescriptors:
  print d + ', ' + str(countByDescriptor[d])
