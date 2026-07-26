# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:16:05 2026

@author: Sthuthi Sheela
"""

import heapq
graph={}
n=int(input("Enter the number of nodes: "))
for _ in range(n):
    node=input("Enter the node name: ")
    edges=input(f"Enter the neighbors and costs of {node} :").split()
    neighbors={}
    for i in range(0,len(edges),2):
        neighbors[edges[i]]=float(edges[i+1])
    graph[node]=neighbors
heuristic={}
for node in graph:
    h=int(input(f"ENter the heuristic value for {node}: "))
    heuristic[node]=h
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
def a_star(start,goal):
    visited=set()
    pq=[]
    heapq.heappush(pq,(heuristic[start],0,start,[start]))
    while pq:
        f_score,g_score,node,path=heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        print(f"Visiting : {node} , g={g_score},f={f_score}")
        if node==goal:
            print("\nGoal reached!")
            print("Path: ","->".join(path))
            print("Total Cost: ",g_score)
            return path,g_score
        for neighbor,cost in graph[node].items():
            if neighbor not in visited:
                g_new=g_score+cost
                f_new=g_new+heuristic[neighbor]
                heapq.heappush(pq,(f_new,g_new,neighbor,path+[neighbor]))
a_star(start,goal)