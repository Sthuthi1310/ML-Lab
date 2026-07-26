# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:16:22 2026

@author: Sthuthi Sheela
"""
import numpy as np
list1=[1,2,3,4]
array1=np.array(list1)
print(list1)
print(array1)#numpy array
print(array1*2)#multiplies 
print(list1*2)#repeats twice

list2=[2,4,6.6,"apple",10]
print(np.array(list2))
list3=[11,13,15,234,353]
print(np.array(list3,dtype=float))

#2D array
list4=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
array4=np.array(list4)
print(list4)
print(array4)

