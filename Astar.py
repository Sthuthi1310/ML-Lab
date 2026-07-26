# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:52:53 2026

@author: Sthuthi Sheela
"""

import heapq

graph = {}
heuristic = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    neighbours = {}

    m = int(input(f"Enter number of neighbours for {node}: "))

    for j in range(m):
        neighbour = input("Enter neighbour: ")
        cost = int(input("Enter cost: "))
        neighbours[neighbour] = cost

    graph[node] = neighbours

for node in graph:
    h = float(input(f"Enter heuristic value for {node}: "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def a_star_search(start, goal):
    visited = set()

    pq = []

    heapq.heappush(
        pq,
        (heuristic[start], 0, start, [start])
    )

    while pq:

        f_score, g_score, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        print(
            f"Visiting: {node}, "
            f"g={g_score}, "
            f"f={f_score}"
        )

        if node == goal:
            print("\nGoal reached!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g_score)

            return path, g_score

        for neighbour, cost in graph[node].items():

            if neighbour not in visited:

                g_new = g_score + cost

                f_new = g_new + heuristic[neighbour]

                heapq.heappush(
                    pq,
                    (
                        f_new,
                        g_new,
                        neighbour,
                        path + [neighbour]
                    )
                )


a_star_search(start, goal)