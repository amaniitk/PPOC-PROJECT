#1
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A","B","C"])
y=np.array([2,3,4])
c = np.array(["red","blue","green"])
plt.bar(x,y,color=c)
plt.show()

#2
import numpy as np
import matplotlib.pyplot as plt
name = np.array(['radha','harsh','medha','sparsh'])
math_marks = np.array([25,27,26,19])
phy_marks = np.array([23,27,29,21])
chm_marks = np.array([19,23,25,20])
total_marks = np.add(math_marks,phy_marks,chm_marks)
plt.bar(name,total_marks,color = "darkslateblue")
plt.title("performance in class")
plt.xlabel("name")
plt.ylabel("total marks out of 90")
plt.show()

#3
import numpy as np
import matplotlib.pyplot as plt
x= np.array([25,7,8,17,2,17,2,9,45,78,35,28])
y = np.array([86,84,94,110,23,48,37,84,5,9,24,9])
plt.scatter(x,y,color = 'red')
plt.plot(x,y)
plt.show()

# 4
import numpy as np

arr = np.array([1, 2, 5, 3])
arr1 = np.array([4, 6, 8, 2])
sum = 0
multiplication = 1
for i in arr:
    sum = sum + i

print(sum)  # addition of elements in array
for i in arr:
    multiplication = multiplication * i

print(multiplication)  # multiplication of array elements
newarr1 = np.add(arr, arr1)  # addition of two arrays
print(newarr1)
newarr2 = np.subtract(arr, arr1) # subtraction of two arrays
print(newarr2)
newarr3 = np.prod([arr, arr1])  # multiplication of two arrays
print(newarr3)


