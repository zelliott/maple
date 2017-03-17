# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:48:22 2017

@author: omarpaladines
"""

import csv

# construct the map
file = open('test_output/nytimes_cloze_tests.txt', 'r')
lines = file.readlines()
ppl_map = dict()
for line in lines[1:]:
    ppl = float(line.split(',')[5])
    index = float(line.split(',')[0])
    ppl_map[index] = ppl

# add stuff to the CSV 
fr = open("clozeAbstracts.csv", "r")
wr = open("clozeAbstractsPPL.csv", "w")
csv_reader = csv.reader(fr, delimiter=',')
csv_writer = csv.writer(wr, lineterminator='\n')
all_ = []
for i in xrange (0, 545) :
    row = csv_reader.next()
    row.append(ppl_map[i])
    all_.append(row)

csv_writer.writerows(all_)