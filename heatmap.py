import matplotlib.pyplot as plt
import seaborn as sns

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sns.heatmap(data, annot=True)

plt.title("Heat Map")
plt.show()