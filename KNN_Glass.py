# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:31:37 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
url="http://10.24.30.48/dataset/glass.csv"
data=pd.read_csv(url)
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
metrics=['euclidean','manhattan']
for metric in metrics:
    print("\n=========================================")
    print("Distance Metrix: ",metric)
    print("\n=========================================")
    knn=KNeighborsClassifier(
        n_neighbors=3,
        metric=metric)
    knn.fit(X_train,y_train)
    y_pred=knn.predict(X_test)
    print("Accuracy score: ",accuracy_score(y_test,y_pred))
    print("Confusion matrix: \n",confusion_matrix(y_test,y_pred))
    