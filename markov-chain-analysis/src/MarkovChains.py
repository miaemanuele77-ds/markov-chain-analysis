#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 17:40:21 2025

@author: miaemanuele
"""
##--- Construct a transition matrix 𝑃 (as a numpy array) to model
##- this single player snakes-andladders game as a Markov Chain:

import numpy as np
P = np.array([
# (present state) from 0    1    2    3    4    5    6    7    8   (next state)
                     [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0],  # to 0
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 1
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 2
                     [0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0],  # to 3
                     [0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 4
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 5
                     [0.5, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0],  # to 6
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 7
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0],  # to 8
])

print(P)

#############

##-- The expected number of coin flips needed to reach square 𝑘 from square 𝑖:

N = np.array([
# (present state) from 0    1    2    3    4    5    6    7   (next state
                     [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0],  # to 0
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 1
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 2
                     [0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.0],  # to 3
                     [0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0],  # to 4
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 5
                     [0.5, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0],  # to 6
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # to 7
])

print(N)



I = np.eye(8)
print(I)
print(I.shape)


D= I-N
print(D)

F = np.linalg.inv(D)
print(F)

##############


##-- Expected number of coin flips required to reach the absorbing 
##-- state from each starting position

F = np.array(F)
sum_of_columns = np.sum(F,axis=0).tolist() 
print(sum_of_columns)



