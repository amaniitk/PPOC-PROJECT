import matplotlib.pyplot as plt
features = ['A', 'B', 'C']
values = [2, 3, 4]
colors = ['red', 'blue', 'green']
plt.bar(features, values, color=colors)
plt.title('Bar Graph')
plt.xlabel('Variables')
plt.ylabel('Values')
plt.show()

import matplotlib.pyplot as plt
features = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 5]
plt.bar(features, values)
plt.title('Example Bar Graph')
plt.xlabel('Variables')
plt.ylabel('Values')
plt.show()

import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 8, 9]
plt.scatter(x_values, y_values, color='red')
for i in range(len(x_values)-1):
    plt.plot([x_values[i], x_values[i+1]], [y_values[i], y_values[i+1]], color='blue')
plt.title('Scattered Points with Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

import numpy as np
arr = np.array([1, 2, 5, 3])
addition = arr + 2
subtraction = arr - 1
multiplication = arr * 3
print('Original array:', arr)
print('Array after addition:', addition)
print('Array after subtraction:', subtraction)
print('Array after multiplication:', multiplication)
