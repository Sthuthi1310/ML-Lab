# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:24:45 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load dataset from URL
url = "http://10.24.30.48/dataset/fruit.csv"
df = pd.read_csv(url)

# Display first 5 rows
print("Dataset:")
print(df.head())

# Select only numeric columns
X = df.select_dtypes(include=['int64', 'float64'])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(X_scaled)

# Create DataFrame for PCA result
pca_df = pd.DataFrame(
    data=principal_components,
    columns=['PC1', 'PC2']
)

print("\nPCA Result:")
print(pca_df.head())

# Explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Plot PCA
plt.figure(figsize=(8,6))
plt.scatter(pca_df['PC1'], pca_df['PC2'])

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Fruit Dataset")

plt.show()