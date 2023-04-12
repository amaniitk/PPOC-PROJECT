import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_file = pd.read_csv('C:/Users/Shrimi Agrawal/Downloads/archive.zip')
print(data_file.to_string())
p = data_file['Global Score 2021'].max()
q = data_file['Global Score 2019'].min()
x = np.array(["worst Global Score of 2021","best Global Score of 2019 "])
y = np.array([p,q])
plt.bar(x,y)
plt.show()