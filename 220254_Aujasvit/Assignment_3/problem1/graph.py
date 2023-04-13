import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def sigmoid(a):
  return 1/(1 + np.exp(-1*a))

def tanh(a):
  return (np.exp(a) - np.exp(-a))/(np.exp(a) + np.exp(-a))

x = np.linspace(-10, 10, 1000000)

plt.plot(x, sigmoid(x))
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.show()

plt.plot(x, tanh(x))
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.show()
