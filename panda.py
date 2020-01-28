#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:18:21 2019

@author: apple
"""



diccio =  {"pais": ["Brasil", "Rusia", "India", "China", "Sur Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "poblacion": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd

paises = pd.DataFrame(diccio)

paises.index = ["BR", "RU", "IN", "CH", "SA"]

print(paises)
print("------series------")
# Print out country column as Pandas Series
print(type(paises['capital']))
print("------dataframe------")

# Print out country column as Pandas DataFrame
print(type(paises[['capital']]))
print("------dataframe------")

# Print out DataFrame with country and drives_right columns
print(paises[['pais', 'capital']])


cars = pd.read_csv('carros.csv')

print("------carros------")
print(cars)


print("------carros 0:4------")

# Print out first 4 observations
print(cars[0:4])
print("------4:6------")

# Print out fifth, sixth, and seventh observation
print(cars[4:6])


# Print out observation for Japan
print(cars.iloc[2])
print("------4cambiando------")

cars.set_index('id',inplace=True)
print("------4:6------")


# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
