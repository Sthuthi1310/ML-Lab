import matplotlib.pyplot as plt
import seaborn as sns

data = [
    [10, 22, 33],
    [4, 50, 16],
    [27, 8, 19]
]

sns.heatmap(data, annot=True)

plt.title("Heat Map")
plt.show()