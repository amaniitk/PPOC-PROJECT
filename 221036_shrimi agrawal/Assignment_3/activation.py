import numpy as np
from cmath import exp
import collections.abc
import matplotlib.pyplot as plt
value = input("enter the type of data: ")
if(value == "array"):
  a = int(input("size of array: "))
  my_arr = ([])
  for i in range(a):
     x = float(input("element: "))
     my_arr = np.append(my_arr,x)

  if(isinstance((np.array(my_arr)),(collections.abc.Sequence,np.ndarray)) == True):
      def sigmoid(z):
          return 1 / (1 + np.exp(-z))

      def tanh(z):
          return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

  sigmoid_arr = sigmoid(my_arr)
  tanh_arr =tanh(my_arr)
  print(sigmoid_arr)
  print(tanh_arr)

else:
 b = int(input("enter the real number: "))
def sigmoid_first(z):
      return 1/(1+2.71**(z))

def tanh_first(z):
 return  (2.71**(z)-2.71**(-z))/(2.71**(z)+2.71**(-z))
print(sigmoid_first(b))
print(tanh_first(b))








