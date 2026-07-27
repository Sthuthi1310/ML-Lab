# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:44:53 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.naive_bayes import GaussianNB
url="http://10.24.30.48/dataset/Titanic.csv"
data=pd.read_csv(url)
X=data[['Pclass','Sex','Age','Fare']].copy()
Y=data['Survived']
X['Age']=X['Age'].fillna(X['Age'].mean())
le=LabelEncoder()
X['Sex']=le.fit_transform(X['Sex'])
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy: ",accuracy_score(y_test,y_pred))
print("Confusion Matrix: ")
print(confusion_matrix(y_test,y_pred))
