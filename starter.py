import stringOperations
import csv
import numpy as np

class first():
    """comments = []
    labels = []"""
    obj1 = stringOperations.stringOperationsStart()
    def __init__(self):
        return
        

    """with open('../files/training.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            comments.append(row[3])
            if row[2] == 'Sad':
                labels.append(-1)
            elif row[2] == 'Happy':
                labels.append(1)
            else:
                labels.append(0)
            line_count += 1

    counter = 0
    for sentence in comments: """
    """sentence = "bu harika cumleyi salak gonderip  salak duzenlemeyecegiz mukemml gelmek ay bayıldım hafta lakin bunu sevemedim yalnız"""
    def extract_features(self,sentence):
        features = []
        cumledekiKelimeler = [];
        self.obj1.stringiDegis(sentence)
        sentence = self.obj1.normalize()
        cumledekiKelimeler = self.obj1.tokenize(sentence)
        cumledekiKelimeler = self.obj1.negatifler(cumledekiKelimeler)
        cumledekiKelimeler = self.obj1.pozitifler(cumledekiKelimeler)
        self.obj1.morfoloji(cumledekiKelimeler)
        self.obj1.zamanveBaglacIceriyorMu(cumledekiKelimeler)
        features.append(self.obj1.olumsuzSayisi(cumledekiKelimeler))
        features.append(self.obj1.olumluSayisi(cumledekiKelimeler))
        features.append(self.obj1.baglacSayisi(cumledekiKelimeler))
        features.append(self.obj1.notSayisi(cumledekiKelimeler))
        features.append(self.obj1.zamanIceriyorMu(cumledekiKelimeler))
        #features.append(self.obj1.bigramToplamlari(cumledekiKelimeler))
        return features
        """features.append(labels[counter])
        counter += 1
        temp_features = features"""


        """with open('../files/features.csv', 'a') as fd:
            fd.write( str(features)[1:len(str(features))-1] + "\n")"""
        """features.append(obj1.bigramToplamlari(cumledekiKelimeler))"""
        #print(features)



