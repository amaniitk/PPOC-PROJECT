import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Marks in various subjects
math = pd.Series([94, 98, 64], index = ["Jon", "Jane", "Charlie"])
science = pd.Series([88, 82, 60], index = ["Jon", "Jane", "Charlie"])
sst = pd.Series([79, 66, 80], index = ["Jon", "Jane", "Charlie"])

x = np.arange(3)
df = pd.DataFrame({'Math': math, 'Science': science, "SST": sst})

plt.bar(x - 0.1, df['Math'].values, width = 0.1)
plt.bar(x, df['Science'].values, width = 0.1)
plt.bar(x + 0.1, df['SST'].values, width = 0.1)
plt.xticks(x, ['Jon', 'Jane', 'Aujasvit'])
plt.xlabel('Student')
plt.ylabel('Marks')
plt.legend(['Math', 'Science', 'SST'])
plt.show()
