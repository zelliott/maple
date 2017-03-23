# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:20:57 2017

@author: omarpaladines
"""

import numpy as np
from sklearn import linear_model


def fit(train_file, num_features):    
    # load the data
    csv_file = np.genfromtxt (train_file, delimiter=",")
    
    X = np.array(csv_file[:, 1 : num_features + 1])
    y = np.array(csv_file[:,0])
    
    # initialize the model
    reg = linear_model.LinearRegression()   
    reg.fit(X, y)
    return reg    
    
def predict (model, X_test) :
    return model.predict(X_test)
