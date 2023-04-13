from math import *
import numpy as np

def Activation(X,Y,Z):
    if Z == 1:
        if Y == 1:
            return 1/(1+exp(-X))
        elif Y==2:
            list = []
            for i in X:
                j = float(i)
                list.append(1/(1+exp(-j)))
            return np.array(list)
    elif Z == 2:
        if Y == 1:
            return (exp(X)-exp(-X))/(exp(X)+exp(-X))
        elif Y==2:
            list = []
            for i in X:
                j = float(i)
                list.append(tanh(int(i), 1))
            return np.array(list)

print("1 for Real Number, 2 for array:\n")
print("1 for Sigmoid, 2 for Hyperbolic Tangent:\n")

L = input("Enter the preference Separated by Comma, Ex: 1,2.\n").split(',')

if int(L[0])==1:
    A = int(input("Enter the Number:"))
    print(Activation(A,int(L[0]),int(L[1])))
elif int(L[0])==2:
    A = []
    for i in input("Enter the Numbers:").split(","):
        A.append(i)
    A = np.array(A)
    print(Activation(A,int(L[0]),int(L[1])))