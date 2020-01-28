#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:21:34 2019

@author: apple
"""

def magica(prim, sec, *otros):
    return (prim+sec), len(otros)


def magica2(prim, sec, **otros):
    if otros.get("clave") == "ok":
        return "bien"
    else:
        return "mal"

print(magica(1,2,4,5,6))

print(magica2(1,2,clave="ok"))

    