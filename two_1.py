from matplotlib import pyplot as plt

features = ['A','B','C']
values = [2,3,4]
colors = ["Red","Blue","Green"]

plt.style.use("fivethirtyeight")

plt.bar(features, values, color=colors)

plt.xlabel("features")
plt.ylabel("values")
plt.show()