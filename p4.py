# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:48:18 2026

@author: Sthuthi Sheela
"""

import pandas as pd

df = pd.read_csv("fruits.csv")
print(df)
print("------------")
print(df.loc[0])
print("------------")
print(df.loc[3])
print("------------")
print(df.iloc[[0,3]])
print("-------------")
df.insert(3,'taste',['s','s','s','s','s']) # (colnum after which new col taste has to be inserted, col name and value)
print(df)
print("-------------")