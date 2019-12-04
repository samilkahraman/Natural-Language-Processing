import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from nltk.classify import maxent
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score


class MaxEnt():
	train = []
	classifier = ''
	eval_classifier = ''
	eval_test = []
	y_test = []

	def __init__(self,type):
		if type == 1:
			with open("features.csv") as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				line_count = 0
				for row in csv_reader:
					if line_count == 0:
						line_count+=1
					else:
						feature_label = ()
						features = {}
						for i in range(len(row)-2):
							features['f'+str(i)] = float(row[i])
							line_count += 1
							feature_label = (features,int(row[len(row)-1]))
							self.train.append(feature_label)
			print("training maxent...")
			self.classifier = maxent.MaxentClassifier.train(self.train, algorithm='iis', trace=0, max_iter=3)
			print("maxent training done.")
		else:
			with open("features.csv") as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				line_count = 0
				for row in csv_reader:
					if line_count == 28800:
						break
					if line_count == 0:
						line_count+=1
					else:
						feature_label = ()
						features = {}
						for i in range(len(row)-2):
							features['f'+str(i)] = float(row[i])
							line_count += 1
							feature_label = (features,int(row[len(row)-1]))
							self.train.append(feature_label)
			print("eval training maxent...")
			self.eval_classifier = maxent.MaxentClassifier.train(self.train, algorithm='iis', trace=0, max_iter=3)
			with open("features.csv") as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				line_count = 0
				
				for row in csv_reader:
					if line_count <= 28800:
						line_count += 1
					else:
						features = {}
						for i in range(len(row)-2):
							features['f'+str(i)] = float(row[i])
							line_count += 1
							self.eval_test.append(features)
							self.y_test.append(int(row[len(row)-1]))

			y_pred = self.eval_classifier.classify_many(self.eval_test)
			print(confusion_matrix(self.y_test,y_pred))
			print(classification_report(self.y_test,y_pred))
		

	def predict_max_ent(self,features):
		
		features_ = {}
		test = []
		for i in range(len(features)):
			features_['f'+str(i)] = float(features[i])
		test.append(features_)
		

		return self.classifier.classify_many(test)






