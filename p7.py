# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:59:08 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Dataset paths
glass_path = "http://10.24.30.48/dataset/glass.csv"
fruit_path = "http://10.24.30.48/dataset/fruit.csv"

def run_knn(dataset_path, dataset_name):
    print("\n====================")
    print(f"DATASET: {dataset_name}")
    print("====================")

    # Load dataset
    data = pd.read_csv(dataset_path)

    print("\nColumns in dataset:")
    print(data.columns)

    # Drop ID column if exists
    if "id" in data.columns:
        data = data.drop("id", axis=1)

    # Identify target column
    if dataset_name == "Fruit":
        if "fruit_label" in data.columns:
            target_col = "fruit_label"
        elif "fruit_name" in data.columns:
            target_col = "fruit_name"
        else:
            target_col = data.columns[-1]
    else:
        target_col = data.columns[-1]

    # Split features and target
    X = data.drop(target_col, axis=1)
    y = data[target_col]

    # Convert target if needed
    if y.dtype == "float64":
        y = y.astype("int")

    # Scale features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Train-test splits
    splits = [(0.1, "90-10"), (0.3, "70-30")]
    k_values = [3, 5, 7]

    distance_metrics = {
        "Euclidean": "euclidean",
        "Manhattan": "manhattan"
    }

    for test_size, split_name in splits:
        print("\n----------------------")
        print(f"Train-Test Split: {split_name}")
        print("----------------------")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        for metric_name, metric in distance_metrics.items():
            print(f"\nDistance Metric: {metric_name}")

            for k in k_values:
                model = KNeighborsClassifier(n_neighbors=k, metric=metric)
                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                acc = accuracy_score(y_test, y_pred)
                cm = confusion_matrix(y_test, y_pred)

                print(f"\nK = {k}")
                print(f"Accuracy: {acc:.4f}")
                print("Confusion Matrix:")
                print(cm)


# Run for both datasets
run_knn(glass_path, "Glass")
run_knn(fruit_path, "Fruit")
