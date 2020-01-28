#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:13:14 2019

@author: apple
"""

frase = "el coronel no tiene quien le escriba"
palabras = frase.split()
longitudes = []

for palabra in palabras:
    if (palabra != "no"):
        longitudes.append(len(palabra))
    

print(longitudes)
    

longitudes2 = [len(palabra) for palabra in palabras if palabra != "no" ]


print(longitudes2)