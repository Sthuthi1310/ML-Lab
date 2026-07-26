# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:08:09 2026

@author: Sthuthi Sheela
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
from sklearn.preprocessing import StandardScaler
url="http://10.24.30.48/dataset/IRIS.csv"
data=pd.read_csv(url)
X=data.iloc[:,:-1]
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
plt.figure(figsize=(10,5))
linked_single=linkage(X_scaled,method='single')
dendrogram(linked_single)
plt.title("Dendrogram Single linkage")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()
plt.figure(figsize=(10,5))
linked_complete=linkage(X_scaled,method='complete')
dendrogram(linked_complete)
plt.title("Dendrogram Complete")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()