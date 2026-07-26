import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
url = "http://10.24.30.48/dataset/IRIS.csv"
data = pd.read_csv(url)

# Show data
print(data.head())

# Select features (exclude species/label column if present)
X = data.iloc[:, :-1]

# Apply K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Results
print("Centroids:\n", kmeans.cluster_centers_)
print("Labels:\n", kmeans.labels_)

# Plot (first 2 features)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x')
plt.title("K-Means on IRIS Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
