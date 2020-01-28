#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:37:38 2019

@author: apple
"""


def saludo(nombre, int1, int2):
    resulta = int1+int2
    return ("hola %s, el resultado es %d" % (nombre, resulta))


def suma(int1, int2):
    i1 = int(int1)
    i2= int(int2)
    resulta = i1+i2
    return resulta


rta = 'y'

while rta =='y':

    print("Bienvenido a la calculadora")

    
    try:
        n1 = int(input('Ingrese un numero 1'))
    except ValueError:
        print("Oops!  No es un numero valido")
        continue


    try:
        n2 = int(input('Ingrese un numero 2'))
    except ValueError:
        print("Oops!  No es un numero valido")
        continue

    r = suma(n1,n2)
    print ("El resultado es", r)
    
    rta = input('Desea continuar( y/n)')
