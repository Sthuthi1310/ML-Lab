import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
url = "http://10.24.30.48/dataset/fruit.csv"
data = pd.read_csv(url)

# Features and target
X = data[['mass', 'width', 'height', 'color_score']]
y = data['fruit_label']

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=2
)

# Train model
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)

# Predict
y_pred = lda.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted values:")
print(y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Transform data using LDA
X_lda = lda.transform(X)

# Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(X_lda[:,0], y)
plt.title("LDA Scatter Plot")
plt.xlabel("Linear Discriminant")
plt.ylabel("Fruit Label")

plt.show()