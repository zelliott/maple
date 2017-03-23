# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:51:43 2017

@author: omarpaladines
"""

from test_abstract import test_model
from feature_combination import fit 
from feature_combination import predict
import numpy as np

# NEED TO ADD THE OTHER MEASURES HERE
def ppl (abstract) :
    
    # This part should be done asynchronously, before everything
    ml_model = fit ('ppl_nozero.csv', 9)
    
    
    model_dict = [('nytimes_uni','1'), ('nytimes_bi','2'), ('nytimes_tri','3'),
                  ('fisher_uni','1'), ('fisher_bi','2'), ('fisher_tri','3'),
                  ('medline_uni','1'), ('medline_bi','2'), ('medline_tri','3')]
              
    scores = []
    for (model, order) in model_dict :
        scores.append(test_model(abstract, model, order))
    
    return predict(ml_model, np.array(scores).reshape(1,-1)).item(0)
    
#print ppl('0')    