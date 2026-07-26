import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Dataset URLs
datasets = {
    "Glass": "http://10.24.30.48/dataset/glass.csv",
    "Fruit": "http://10.24.30.48/dataset/fruit.csv"
}

# K values
k_values = [3, 5, 7]

# Test sizes (90-10 and 70-30)
test_sizes = [0.1, 0.3]

# Distance metrics
metrics = ['euclidean', 'manhattan']

for name, url in datasets.items():

    print("\n" + "=" * 60)
    print("DATASET :", name)
    print("=" * 60)

    data = pd.read_csv(url)
    print(data.shape)
    print(data.columns)

    # Select Features and Target
    if name == "Fruit":
        X = data.iloc[:, 1:]   # mass, width, height, color_score
        y = data.iloc[:, 0]    # fruit_label
    else:
        X = data.iloc[:, :-1]  # RI, Na, Mg, ...
        y = data.iloc[:, -1]   # Type

    for test_size in test_sizes:

        print("\n" + "-" * 60)
        if test_size == 0.1:
           print("Train-Test Split = 90-10")
        else:
           print("Train-Test Split = 70-30")
           print("-" * 60)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=42
        )

        for metric in metrics:

            print(f"\nDistance Metric : {metric}")

            for k in k_values:

                knn = KNeighborsClassifier(
                    n_neighbors=k,
                    metric=metric
                )

                knn.fit(X_train, y_train)

                y_pred = knn.predict(X_test)

                accuracy = accuracy_score(y_test, y_pred)

                print(f"\nK = {k}")
                print(f"Accuracy = {accuracy:.2f}")

                cm = confusion_matrix(y_test, y_pred)

                print("Confusion Matrix:")
                print(cm)