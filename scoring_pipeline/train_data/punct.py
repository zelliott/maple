# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:22:22 2017

@author: omarpaladines
"""
import nltk
import string
# remove any punctuation before tokenizing.
with open('medline.txt', 'r') as myfile, open('medline_punct.txt', 'w') as outfile:
    data=myfile.read()
    #train_data = data.encode('utf-8').translate(None, string.punctuation)
    train_data = data.translate(None, string.punctuation)
    train_data = nltk.word_tokenize(train_data)
    count = 0
    for token in train_data :
        count+=1
        outfile.write(token + " ")
        if (count == 10) :
            outfile.write("\n")
            count = 0
