import numpy as np
import matplotlib.pyplot as plt
data=np.random.rand(10,5)
plt.figure(figsize=(8,6))
plt.boxplot(data)
plt.title("Box plot")
plt.xlabel("Features")
plt.ylabel("Values")
plt.show()