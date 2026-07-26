# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:12:29 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
url="http://10.24.30.48/dataset/IRIS.csv"
data=pd.read_csv(url)
X=data.iloc[:,:-1]
Kmeans=KMeans(n_clusters=3)
KMeans.fit(X)
print("Centroids: \n",Kmeans.cluster_centers_)
print("Labels: \n",Kmeans.labels_)
plt.scatter(X.iloc[:,0],X.iloc[:,1],c=Kmeans.label_)
plt.scatter(Kmeans.cluster_centers[:,0],Kmeans.cluster_centers_[:,1],marker='X')
plt.title("K Means cluster")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
