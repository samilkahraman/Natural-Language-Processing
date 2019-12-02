import re
from nltk.util import ngrams
import csv

class Bigrams():

    comments = []
    def __init__(self):
        with open('training.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                    self.comments.append(row[3].lower())
                    line_count += 1
            print(f'Processed {line_count} lines.')

    def generate_ngrams(self,s, n):
        # Convert to lowercases
        s = s.lower()
        
        # Replace all none alphanumeric characters with spaces
        s = re.sub(r'[^a-zA-Z0-9_ğüşıöçĞÜŞİÖÇ\s]', ' ', s)
        
        # Break sentence in the token, remove empty tokens
        tokens = [token for token in s.split(" ") if token != ""]
        
        # Use the zip function to help us generate n-grams
        # Concatentate the tokens into ngrams and return
        ngrams = zip(*[tokens[i:] for i in range(n)])
        return [" ".join(ngram) for ngram in ngrams]

    def all_words(self):

        all_word_count = 0
        for comment in self.comments:
            for word in comment.split(" "):
                all_word_count+=1
        return all_word_count

    def calculate_bigram(self,word_pre,word_post):

        word_pre = word_pre.lower()
        word_post = word_post.lower()
        bigram_count = 0
        total_count = 0
        total_word_count = self.all_words()

        for comment in self.comments:
            for x in self.generate_ngrams(comment,2):
                if x == word_pre+" "+word_post:
                    bigram_count+=1
        if bigram_count == 0:
            bigram_count+=1
        for comment in self.comments:
            if comment.find(word_post):
                total_count +=1
        total_count += total_word_count
        return bigram_count/total_count
        
        

   








