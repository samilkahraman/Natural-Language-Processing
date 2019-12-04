import csv
import nltk 

class NaiveBayes():
    comments = []
    sentiments = []
    all_word_count = 0
    positive_prob = 0
    negative_prob = 0
    neutral_prob = 0
    def __init__(self):
        with open('training.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                    self.comments.append(row[3].lower())
                    self.sentiments.append(row[2])
                    line_count += 1
            """print(f'Processed {line_count} lines.')"""
        self.all_word_count = self.all_words_n()
        self.positive_prob = self.positive()
        self.negative_prob = self.negative()
        self.neutral_prob = self.neutral()


    def all_words_n(self):
        all_word_count = 0
        for comment in self.comments:
            for word in comment.split(" "):
                all_word_count+=1
        return all_word_count

    def positive(self):
        count = 0;
        for sentiment in self.sentiments:
            if(sentiment == 'Happy'):
                count+=1
        return count/len(self.sentiments)

    def negative(self):
        count = 0;
        for sentiment in self.sentiments:
            if(sentiment == 'Sad'):
                count+=1
        return count/len(self.sentiments)

    def neutral(self):
        count = 0;
        for sentiment in self.sentiments:
            if(sentiment == 'Neutral'):
                count+=1
        return count/len(self.sentiments)

    def predict_negative(self,comment,all_word_count):
        value = 1
        for word in comment.split(" "):
            count = 0;
            for i in range(len(self.comments)):
                if self.sentiments[i] == 'Sad':
                    for word2 in self.comments[i].split(" "):
                        if(word == word2):
                            count+=1
            
            count += 0.00001
            value *= count/(all_word_count+all_word_count/2)
        return value*self.negative_prob

    def predict_positive(self,comment,all_word_count):
        value = 1
        for word in comment.split(" "):
            count = 0;
            for i in range(len(self.comments)):
                if self.sentiments[i] == 'Happy':
                    for word2 in self.comments[i].split(" "):
                        if(word == word2):
                            count+=1
            
            count += 0.00001
            value *= count/(all_word_count+all_word_count/2)
        return value*self.positive_prob

    def predict_neutral(self,comment,all_word_count):
        value = 1
        for word in comment.split(" "):
            count = 0;
            for i in range(len(self.comments)):
                if self.sentiments[i] == 'Neutral':
                    for word2 in self.comments[i].split(" "):
                        if(word == word2):
                            count+=1
            
            count += 1
            value *= count/(all_word_count*2)
        return value*self.neutral_prob



    def predict_naive_bayes(self,comment):
        
        pr_positive = self.predict_positive(comment,self.all_word_count)
        pr_negative = self.predict_negative(comment,self.all_word_count)
        pr_neutral = self.predict_neutral(comment,self.all_word_count)
        max_ = max(pr_positive,pr_negative,pr_neutral)
        if max_ == pr_neutral:
            return "Neutral"

        elif max_ == pr_positive:
            return "Happy"

        else:
            return "Sad"

















