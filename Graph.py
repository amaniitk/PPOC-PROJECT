import matplotlib.pyplot as plt
from math import exp

plt.style.use("fivethirtyeight")
list_i = []
for i in range(-100,100,1):
    list_i.append(i/10)

list_o1 = []
list_o2 = []
for i in list_i:
    list_o1.append(1/(1+exp(-i)))
    list_o2.append((exp(i)-exp(-i))/(exp(i)+exp(-i)))
plt.plot(list_i, list_o1, label="Sigmoid", linewidth=1)
plt.plot(list_i, list_o2, label="Hyperbolic Tangent",linewidth=1)

plt.title("Sigmoid and Hyperbolic Tangent")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.tight_layout()
plt.show()