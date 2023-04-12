import numpy as np
import matplotlib.pyplot as plt
def sigmoid(z):
    result = 1 / (1 + np.exp(-z))
    return result

def Tanh(z):
    result = (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))
    return result



x = np.linspace(-10, 10, 100)
y1 = sigmoid(x)
y2 = Tanh(x)
plt.plot(x, y1, label='Sigmoid')
plt.plot(x, y2, label='Tanh')
plt.xlabel('z')
plt.ylabel('Function Value')
plt.title('Sigmoid and Tanh Functions')
plt.legend()
plt.show()
