import pandas as pb
import matplotlib.pyplot as plt
import numpy as np
Data = pb.read_csv('World Press Index 2021.csv')

G2021 = []
for i in Data['Global Score 2021']:
    G2021.append(i)

G2020 = []
for i in Data['Global Score 2020']:
    G2020.append(i)

G2019 = []
for i in Data['Global Score 2019']:
    G2019.append(i)
width = 0.4

plt.style.use('fivethirtyeight')

X1 = [2019,2020,2021]
X = np.array(X1)
A = [max(G2019),max(G2020),max(G2021)]
B = [min(G2019),min(G2020),min(G2021)]

plt.bar(X-width/2, A, width=width, label = "Max")
plt.bar(X+width/2, B, width=width, label = "Min")

plt.xticks(X)
plt.title("Global Press Freedom Score\n from 2019 to 2021")
plt.xlabel("Years")
plt.ylabel("Global Score")
plt.legend()

plt.tight_layout()
plt.show()