# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:52:48 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

url = "http://10.24.30.48/dataset/fruit.csv"
df = pd.read_csv(url)

X = df[['mass','width','height','color_score']]

X = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:,0], X_pca[:,1])
plt.title("PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()