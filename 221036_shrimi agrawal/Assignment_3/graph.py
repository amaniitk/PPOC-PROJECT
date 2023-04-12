import numpy as np
from numpy import random
import matplotlib.pyplot as plt
#graph 1
def sigmoid(z):
    return 1/(1+2.71**(-z))
x = np.linspace(-50,50,150)#generate random uniform values
y = sigmoid(x)
plt.plot(x,y)
plt.title("sigmoid graph")
plt.show()
#graph 2
def tanh(z):
    return (2.71**(z)-2.71**(-z))/(2.71 **(z) + 2.71**(-z))
x = np.linspace(-50,50,150)#generate random uniform values
y = tanh(x)
plt.plot(x,y)
plt.title("tanh graph")
plt.show()

