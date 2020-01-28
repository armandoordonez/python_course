#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:27:32 2019

@author: jaordonez
"""


numeros = 1 + 2 * 3/ 4

print(numeros)

remanente = 11 %3

print(remanente)

cuadrado = 7**2

print(cuadrado)


cubo = 5 ** 3

print(cubo)


holamundo = "hola" + " " + "mundo"

print(holamundo)

varias =  "ja" * 3
print(varias)


pares = [2,4,6]
impares = [1,3,5]

todos = pares + impares

print(todos)

cadena = pares * 3

print(cadena)



#Python 3.7.0 (default, Jun 28 2018, 07:39:16)
#Type "copyright", "credits" or "license" for more information.
#
#IPython 7.10.1 -- An enhanced Interactive Python.
#
#runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#[1, 2, 3]
#2
#
#runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#[1, 2, 3]
#1
#
#runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#[1, 2, 3]
#1
#2
#3
#
#runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#[1, 2, 3]
#1
#2
#3
#Traceback (most recent call last):
#
#  File "<ipython-input-4-2551d4473516>", line 1, in <module>
#    runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#
#  File "/Users/apple/anaconda3/envs/spider336/lib/python3.7/site-packages/spyder_kernels/customize/spydercustomize.py", line 827, in runfile
#    execfile(filename, namespace)
#
#  File "/Users/apple/anaconda3/envs/spider336/lib/python3.7/site-packages/spyder_kernels/customize/spydercustomize.py", line 110, in execfile
#    exec(compile(f.read(), filename, 'exec'), namespace)
#
#  File "/Users/apple/Desktop/python_tutorial/listas.py", line 16, in <module>
#    for x in mylist:
#
#NameError: name 'mylist' is not defined
#
#
#
#
#runfile('/Users/apple/Desktop/python_tutorial/listas.py', wdir='/Users/apple/Desktop/python_tutorial')
#[1, 2, 3]
#1
#2
#3
#1
#2
#3
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#125
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#125
#hola mundo
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#125
#hola mundo
#jajaja
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#125
#hola mundo
#jajaja
#[2, 4, 6, 1, 3, 5]
#
#runfile('/Users/apple/Desktop/python_tutorial/operadores.py', wdir='/Users/apple/Desktop/python_tutorial')
#2.5
#2
#49
#125
#hola mundo
#jajaja
#[2, 4, 6, 1, 3, 5]
#[2, 4, 6, 2, 4, 6, 2, 4, 6]