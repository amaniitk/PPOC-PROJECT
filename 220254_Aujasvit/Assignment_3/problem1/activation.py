import numpy as np


def sigmoid(a):
  return 1/(1 + np.exp(-1*a))

def tanh(a):
  return (np.exp(a) - np.exp(-a))/(np.exp(a) + np.exp(-a))
