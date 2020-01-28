#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:03:42 2019

@author: apple
"""

from functools import partial

def multiply(x,y):
        return x * y

# Crear una nueva función que multiplica por dos
dbl = partial(multiply,5)
print(dbl(3))