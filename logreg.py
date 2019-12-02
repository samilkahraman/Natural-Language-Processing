import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score


bankdata = pd.read_csv("sonuclar.csv")
X = bankdata.drop('Class', axis=1)
y = bankdata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
print("eval training logreg started...")
eval_svclassifier = LogisticRegression(solver='lbfgs', multi_class='auto')
eval_svclassifier.fit(X_train, y_train)
y_pred = eval_svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
		

		

