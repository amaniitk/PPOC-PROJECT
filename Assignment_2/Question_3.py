
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

x = [1,2,3,4,5,6,7,8,9]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2]

plt.plot(x, y, 'r', linewidth = 1)
plt.scatter(x,y, c='Red')
plt.title('Question 3')
plt.xlabel('X-Coordinates')
plt.ylabel('Y-Coordinates')

plt.tight_layout()

plt.show()