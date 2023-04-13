from math import exp
import numpy as np

def sigmoid(a, q):
    if q == 1:
        return 1/(1+exp(-a))
    elif q==2:
        list = []
        for i in a:
            j = float(i)
            list.append(sigmoid(int(i), 1))
        return np.array(list)

def tanh(a,q):
    if q == 1:
        x,y = exp(a), exp(-a)
        return (x-y)/(x+y)
    elif q==2:
        list = []
        for i in a:
            j = float(i)
            list.append(tanh(int(i), 1))
        return np.array(list)

Q1 = int(input("1 for Real Number, 2 for array:\n"))
Q2 = int(input("1 for Sigmoid, 2 for Hyperbolic Tangent:\n"))
if Q1 == 1:
    Input = int(input("Enter the Number:"))
    if Q2 == 1:
        print(sigmoid(Input,Q1))
    elif Q2 == 2:
        print(tanh(Input,Q1))
elif Q1 == 2:
    a = int(input("How many elements in the array:"))
    list = []
    for i in range(a):
        j = int(input("Enter the Value:"))
        list.append(j)
    arr = np.array(list)
    if Q2 == 1:
        print(sigmoid(arr,Q1))
    elif Q2 == 2:
        print(tanh(arr,Q1))