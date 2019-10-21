import csv
import numpy as np

class IOOperations:


    def duygulariAyir(self, olumsuz=[], olumlu=[], notr=[]):
        with open('training.csv', encoding="utf8") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if(row[2] == 'Sad'):
                    olumsuz.append(row[3])
                elif(row[2] == 'Happy'):
                    olumlu.append(row[3])
                else:
                    notr.append(row[3])
    def yorumlariCsvlereAktar( self, olumluYorumlarAdresi="", olumluYorumlar = []):
        olumluYorumlar = np.array(olumluYorumlar)
        with open(olumluYorumlarAdresi, 'w', newline='') as olumluYorumlar_csv:
            writer = csv.writer(olumluYorumlar_csv,   delimiter=',')
            for x in range(0, olumluYorumlar.shape[0]):
                myList = []
                myList.append(olumluYorumlar[x])
                writer.writerow(myList)
    print("test")
