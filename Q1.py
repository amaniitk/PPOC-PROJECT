import matplotlib.pyplot as plt
from math import *

list = []
list1 = []
list2 = []

for i in range(-50,50,1):
    list.append(i/5)
    list1.append(1/(1+exp(-i/5)))
    list2.append((exp(i/5)-exp(-i/5))/(exp(i/5)+exp(-i/5)))
plt.plot(list, list1, label="Sigm")
plt.plot(list, list2, label="Tanh")
plt.legend()

plt.title("Graphs")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()