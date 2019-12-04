from max_ent import MaxEnt
from naive_bayes import NaiveBayes
from svm import SVM
from starter import first
import csv
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import sys






def result(cls):
	if cls[0] == -1:
		return 'Sad'
	elif cls[0] == 0:
		return 'Neutral'
	else:
		return 'Happy'

def vote(r1,r2,r3):
	count_happy = 0
	count_neutral = 0
	count_sad = 0
	if r1 == 'Happy':
		count_happy+=1
	elif r1 == 'Sad':
		count_sad+=1
	elif r1 == 'Neutral':
		count_neutral+=1
	if r2 == 'Happy':
		count_happy+=1
	elif r2 == 'Sad':
		count_sad+=1
	elif r2 == 'Neutral':
		count_neutral+=1
	if r3 == 'Happy':
		count_happy+=1
	elif r3 == 'Sad':
		count_sad+=1
	elif r3 == 'Neutral':
		count_neutral+=1
	if count_neutral == count_happy and count_neutral == count_sad and count_sad == count_happy:
		return 'Neutral'
	else:
		max_res = max(count_sad,count_happy,count_neutral)
		if max_res == count_neutral:
			return 'Neutral'
		elif max_res == count_sad:
			return 'Sad'
		else:
			return 'Happy'

def vote_without_naive_bayes(r2,r3):
	if r2 != r3:
		return 0
	else:
		return r2	

def predict(comment,features):
	r1 = naive_obj.predict_naive_bayes(comment)
	r2 = svm_obj.predict_svm(features)
	r3 = max_ent_obj.predict_max_ent(features)
	print(r1)
	print(r2)
	print(r3)
	#r2_ = result(r2)
	#r3_ = result(r3)
	#vote_result = vote(r1,r2_,r3_)
	

def predict_without_naive_bayes(features):
	r2 = svm_obj.predict_svm(features)
	r3 = max_ent_obj.predict_max_ent(features)
	vote_result = vote_without_naive_bayes(r2[0],r3[0])
	return vote_result

inputName    = input("Enter input file name: ")
resultName    = input("Enter result file name: ")



stopwords = []		

comments = []
labels = []

with open(inputName) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		comments.append(row[3])
		line_count += 1



y_pred = []
count = 0

parser_obj = first()
max_ent_obj = MaxEnt(1)
naive_obj = NaiveBayes()
svm_obj = SVM(1)



with open(resultName, mode='w') as result_file:
    result_writer = csv.writer(result_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for comment in comments:
    	features = parser_obj.extract_features(comment)
    	result = predict_without_naive_bayes(features)
    	classi = '' 
    	if result == -1:
    		y_pred.append('Sad')
    		classi = 'Sad'
    		print(str(count)+" : Sad")
    		
    	elif result == 0:
    		y_pred.append('Neutral')
    		classi = 'Neutral'
    		print(str(count)+" : Neutral")
    		
    	elif result == 1:
    		y_pred.append('Happy')
    		classi = 'Happy'
    		print(str(count)+" : Happy")
    	result_writer.writerow([comment, classi])
    	count+=1



