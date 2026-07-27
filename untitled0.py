# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 08:25:32 2026

@author: Sthuthi Sheela
"""

import matplotlib.pyplot as plt
import seaborn as sns
data=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
sns.heatmap(data,annot=True)
plt.title("Heatmap")
plt.show()