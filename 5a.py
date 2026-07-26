# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:33:20 2026

@author: Sthuthi Sheela
"""

import math
def minmax(depth,nodeIndex,isMax,values,height):
    if depth==height:
        return values[nodeIndex]
    if isMax:
        return max(minmax(depth+1,nodeIndex*2,False,values,height),minmax(depth+1,nodeIndex*2+1,False,values,height))
    else:
        return min(minmax(depth+1,nodeIndex*2,True,values,height),minmax(depth+1,nodeIndex*2+1,True,values,height))
n=int(input("Enter the number of leaf nodes (in power of 2)"))
values=list(map(int,input("Enter teh leaf node values: ").split()))
height=int(math.log2(n))
result=minmax(0,0,True,values,height)
print("Optimal value of MinMax is : ",result)