#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:37:38 2019

@author: apple
"""



diccio = {}

diccio["juan"] = 1059614593
diccio["mar"] = 1166467140
diccio["est"] = 173633283
diccio["extra"] = 123


print (diccio["extra"])

for key in diccio:
    print(key, '->', diccio[key])



print(type(diccio))

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
     print(key)
    
     

print(type(a_dict))



items = diccio.items


print (items)


for value in diccio.values():
    print(value)


#for clave in diccio.items:
#    print ("la clave %s " %(clave))
    