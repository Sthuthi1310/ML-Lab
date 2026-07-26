# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:30:52 2026

@author: Sthuthi Sheela
""" 

import random

def objective_function(x):
    return -x**2 + 5

def hill_climbing(start_x, step_size, max_iterations):
    current_x = start_x
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        new_x = current_x + random.uniform(-step_size, step_size)
        new_value = objective_function(new_x)

        print(f"Iteration {i+1}: x={new_x:.4f}, f(x)={new_value:.4f}")

        if new_value > current_value:
            current_x = new_x
            current_value = new_value

    print("\nFinal Solution:")
    print(f"x={current_x:.4f}, f(x)={current_value:.4f}")

    return current_x, current_value

best_x, best_value = hill_climbing(
    start_x=0.1,
    step_size=0.5,
    max_iterations=10
)