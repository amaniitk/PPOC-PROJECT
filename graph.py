import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

import matplotlib.pyplot as plt
import numpy as np
from graph import sigmoid, tanh

x = np.linspace(-5, 5, 100)
sigmoid_y = sigmoid(x)
tanh_y = tanh(x)

plt.plot(x, sigmoid_y, label='Sigmoid')
plt.plot(x, tanh_y, label='Tanh')
plt.legend()
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
