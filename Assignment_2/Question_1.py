from matplotlib import pyplot as plt

features = ['A','B','C']
values = [2,3,4]
colors = ["Red","Blue","Green"]

plt.style.use("fivethirtyeight")

plt.bar(features, values, color=colors, label=features)


plt.title("Question 1")
plt.legend()
plt.xlabel("Features")
plt.ylabel("Values")
plt.tight_layout()
plt.show()