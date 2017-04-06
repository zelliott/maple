# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:35:06 2017

@author: omarpaladines

This script append 1 unknown word to the end of a file in another file
"""


def preprocess(input_file, output_file):
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line)
        outfile.write(" zzos")
    

preprocess("train_data/clean/medline_punct.txt", "pre_train/medline_punct.txt")
