# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:30:33 2026

@author: Sthuthi Sheela
"""


import heapq
graph={}
n=int(input("Enter the number of nodes: "))
for _ in range(n):
    node=input("Enter the node name: ")
    neighbors=input(f"Enter the neighbors of {node} seperated by space: ").split();
    graph[node]=neighbors
heuristic={}
for node in graph:
    h=float(input(f"Enter the heuristic value of {node}: "))
    heuristic[node]=h
start=input("Enter the start node: ")
goal=input("Enter the target node: ")
def best_first_search(start,goal):
    visited=set()
    pq=[]
    heapq.heappush(pq,(heuristic[start],start,[start]))
    while pq:
        _,node,path=heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        print("Visiting: ",node)
        if (node==goal):
            print("Goal reached!")
            print("Path: ","->".join(path))
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq,(heuristic[neighbor],neighbor,path+[neighbor]))
best_first_search(start,goal)
                