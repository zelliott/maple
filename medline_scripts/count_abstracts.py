#!/usr/bin/python
#$ -S /usr/bin/python

# This script examines either a single file or a dir of files
# and counts (1) the number of medline citations (i.e. abstracts)
# and (2) the number of citations with mesh headings specified.

import xml.etree.ElementTree as et
import os
import operator

folderPath = '/nlp/data/corpora/medline_data/xml_files'
# folderPath = '/home1/z/zelliott/developer/cis400/test_xml'
# folderPath = '/Users/Zack/Developer/cis400/test_xml'
countAbstracts = 0
countAbstractsWithMesh = 0

def processFile(filename):
  global countAbstracts
  global countAbstractsWithMesh

  tree = et.parse(folderPath + '/' + filename)
  root = tree.getroot()

  # Count each abstract/citation
  for citation in root.iter('MedlineCitation'):
    countAbstracts += 1

    # If this article has a mesh list...
    if len(citation.findall('.//MeshHeadingList')) > 0:
      countAbstractsWithMesh += 1

# for f in os.listdir(folderPath):
processFile('medline15n0778.xml')
# processFile('test_count_abstracts.xml')

print 'abstracts, ' + str(countAbstracts)
print 'abstracts with mesh headings, ' + str(countAbstractsWithMesh)