# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:29:05 2017

@author: omarpaladines
"""

'''
# Parse the language model and convert it into a hash table 
def vocabulary(lang_file) :
    vocab = dict()
    with open(lang_file) as infile:
        for line in infile :
            if ('\t' in line) :
                words = line.split("\t")
                actualword = words[1].split("\n")
                vocab[actualword[0]] = words[0]        
    return vocab
'''

# Parse the language model and convert it into a hash table 
def vocabulary(lang_file) :
    vocab = dict()
    with open(lang_file) as infile:
        for line in infile :
            words = line.split()
            for word in words :
                vocab[word] = word        
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
            
#vocab = vocabulary("srilm_models/nytimes.lm")
#postprocess(vocab, "test_data/clean/algorithms/0", "post_test/algorithms/0")
