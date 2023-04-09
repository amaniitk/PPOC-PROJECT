
from matplotlib import pyplot as plt

Courses = ['MTH','CHM','PHY','TA']
Grades = [7,10,9,9]

plt.style.use("fivethirtyeight")

plt.barh(Courses, Grades)


plt.title("Question 2")
plt.ylabel("Courses")
plt.xlabel("Grades")
plt.tight_layout()
plt.show()