# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:33:05 2021

In this file, there are all useful functions for Lab 1. 

@author: Cédric Fontaine
"""
import numpy as np

def randomWalk(series):
    
    n = series.shape[0] # Number of time series
    N = series.shape[1] # Number of elements
    R = np.empty([n,N])
    R[:,0] = series[:,0] # Initial value
    
    for i in range(n):
        for j in range(1,N):
            
            R[i,j] = R[i,j-1] + series[i,j]
            
    return R
  
def gaussMarkov(series, corrTime):
    
    n = series.shape[0] # Number of time series
    N = series.shape[1] # Number of elements
    R = np.empty([n,N])
    R[:,0] = np.zeros([3]) # Initial value
    eta = np.exp(-1/corrTime) 
    
    for i in range(n):
        for j in range(1,N):
            
            R[i,j] = R[i,j-1]*eta + (1 - eta)*series[i,j]
            
    return R, eta
    
