# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:59:26 2026

@author: Sthuthi Sheela
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score,confusion_matrix
url="http://10.24.30.48/dataset/fruit.csv"
data=pd.read_csv(url)
x=data[['mass','width','height','color_score']]
y=data['fruit_label']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=2)
lda=LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)
y_pred=lda.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("\nPredicted value:")
print(y_pred)
print("\nAccuracy:")
print(accuracy)
print("\nConfusion matrix")
print(confusion_matrix(y_test,y_pred))