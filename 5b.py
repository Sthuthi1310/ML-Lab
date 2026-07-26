# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:41:01 2026

@author: Sthuthi Sheela
"""

import math
def alphabeta(depth,nodeIndex,isMax,values,height,alpha,beta):
    if depth==height:
        return values[nodeIndex]
    if isMax:
        best=-float('inf')
        for i in range(2):
            val=alphabeta(depth+1,nodeIndex*2+i,False,values,height,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=float('inf')
        for i in range(2):
            val=alphabeta(depth+1,nodeIndex*2+i,True,values,height,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best
n=int(input("Enter the number of leaf nodes:"))
values=list(map(int,input("Enter the leaf node values: ").split()))
height=math.log2(n)
result=alphabeta(0,0,True,values,height,-float('inf'),float('inf'))
print("Optimal solution : ",result)