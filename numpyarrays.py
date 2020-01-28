#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:59:21 2019

@author: apple
"""

peso_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

peso_array = np.array(peso_kg)

peso_libras = peso_array/2

print(peso_libras)

rta = peso_array > 90

print(rta)


rta2 = peso_array[peso_array > 90]
print(rta2)

