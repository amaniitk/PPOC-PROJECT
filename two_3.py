
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,6,5,6,5,5]

plt.plot(x, y, 'r', linewidth = 1)
plt.scatter(x,y, c='Red')
plt.xlabel('X-Coordinates')
plt.ylabel('Y-Coordinates')

plt.show()