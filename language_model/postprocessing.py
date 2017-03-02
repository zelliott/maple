# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:29:05 2017

@author: omarpaladines
"""

# Parse the language model and convert it into a hash table 
def vocabulary(lang_file) :
    vocab = dict()
    for line in lang_file :
        if ("\t" in line) :
            words = line.split("\t")
            vocab[words[1]] = words[0]       
    return vocab

# Replace each word out of vocabulary with the unknown token zzso    
def postprocess(vocabulary, input_file, output_file) :
    with open(input_file) as infile, open(output_file, 'w') as outfile:
        for line in infile:
            for word in line.split(): 
                if (word in vocabulary) :
                    outfile.write(word)
                else :
                    outfile.write("zzso")
                outfile.write(" ")
            outfile.write("\n")