# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:01:28 2026

@author: Sthuthi Sheela
"""

import numpy as np
def step_function(x):
    return 1 if x>=0 else 0
def train_perceptron(inputs,targets,learning_rate=0.1,epochs=10):
    weights=np.zeros(inputs.shape[1])
    bias=0
    for epoch in range(epochs):
        for i in range(len(inputs)):
            net_input=np.dot(inputs[i],weights)+bias
            output=step_function(net_input)
            error=targets[i]-output
            weights+=learning_rate*error*inputs[i]
            bias+=learning_rate*error
    return weights,bias
def test_perceptron(inputs,weights,bias):
    print("Inputs\tOutput\n")
    for x in inputs:
        net_input=np.dot(x,weights)+bias
        output=step_function(net_input)
        print(f"{x}\t{output}")
x=np.array([[0,0],[0,1],[1,0],[1,1]])
print("AND Function\n")
and_target=np.array([0,0,0,1])
weights,bias=train_perceptron(x,and_target)
print("Weights: ",weights)
print("Bias: ",bias)
test_perceptron(x,weights,bias)
print("OR Function\n")
or_target=np.array([0,1,1,1])
weights,bias=train_perceptron(x,or_target)
print("Weights: ",weights)
print("Bias: ",bias)
test_perceptron(x,weights,bias)
    
    
    
        
        