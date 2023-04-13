import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

x = pd.read_csv('/content/World Press Index 2021.csv')
temp = np.arange(2)

best_2019 = x['Global Score 2019'].min()
best_2019_country = str(x[x['Global Score 2019'] == best_2019]['Country Name']).split()[1]

worst_2021 = x['Global Score 2021'].max()
worst_2021_country = str(x[x['Global Score 2021'] == x['Global Score 2021'].max()]['Country Name']).split()[1]

plt.bar([worst_2021_country + ': Worst Global Score 2019', best_2019_country + ': Best Global Score 2021'], [worst_2021,best_2019,], width = 0.1)
plt.show()
