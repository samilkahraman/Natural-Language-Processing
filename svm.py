import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score

class SVM():

	eval_svclassifier = ''
	svclassifier = ''

	def __init__(self,type):

		bankdata = pd.read_csv("features.csv")
		X = bankdata.drop('Class', axis=1)
		y = bankdata['Class']

		if type == 1:
			print("training svm...")
			self.svclassifier = SVC(kernel='rbf',gamma='auto')
			self.svclassifier.fit(X, y)
			print("svm training done.")
		else:
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
			print("eval training svm started...")
			self.eval_svclassifier = SVC(kernel='rbf',gamma='auto')
			self.eval_svclassifier.fit(X_train, y_train)
			y_pred = self.eval_svclassifier.predict(X_test)
			print(confusion_matrix(y_test,y_pred))
			print(classification_report(y_test,y_pred))
			

	
	def predict_svm (self,features):
		test = [features]
		y_pred = self.svclassifier.predict(test)
		return y_pred
		

