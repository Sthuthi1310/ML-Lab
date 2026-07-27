import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data=np.random.rand(10,5)
sns.heatmap(data,annot=True)
plt.colorbar()
plt.show()