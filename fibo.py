#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:03:39 2019

@author: apple
"""

def fibo():
    n1 = 1
    n2 = 1
    
    while n2 < 5100:
        yield n1
        n1, n2 = n2, n2+ n1
        
        


for nu1 in fibo():
    print (nu1)
