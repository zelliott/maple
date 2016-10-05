#!/usr/bin/python
#$ -S /usr/bin/python

'''
This script examines either a single file or a dir of files
and counts (1) the number of medline citations (i.e. abstracts)
and (2) the number of citations with mesh headings specified.
'''

import xml.etree.ElementTree as et
import os
import operator
import sys

def processFile(filePath):

  count = 0
  countWithMesh = 0
  tree = et.parse(filePath)
  root = tree.getroot()

  # Count each abstract/citation
  for citation in root.iter('MedlineCitation'):
    count += 1

    # If this article has a mesh list...
    if len(citation.findall('.//MeshHeadingList')) > 0:
      countWithMesh += 1

  return count, countWithMesh

def main():

  count = 0
  countWithMesh = 0

  for f in sys.stdin:
    fileCount, fileCountWithMesh = processFile(f[:-1])
    count += fileCount
    countWithMesh += fileCountWithMesh

  print 'abstracts, ' + str(count)
  print 'abstracts with mesh headings, ' + str(countWithMesh)

if __name__ == "__main__":
  main()
