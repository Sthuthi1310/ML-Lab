# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:50:36 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
url="http://10.24.30.48/dataset/fruit.csv"
data=pd.read_csv(url)
x=data.select_dtypes(include=['int64','float64'])
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
pca=PCA(n_components=2)
principal_components=pca.fit_transform(x_scaled)
pca_df=pd.DataFrame(
    data=principal_components,
    columns=['PC1','PC2']
)
print("PCA Resullt\n")
print(pca_df.head())
print("\nExplained Variance Ration: ")
print(pca.explained_variance_ratio_)
plt.figure(figsize=(8,6))
plt.scatter(pca_df['PC1'],pca_df['PC2'])
plt.xlabel("Principal component 1")
plt.ylabel("Principle Componetn 2")
plt.show()