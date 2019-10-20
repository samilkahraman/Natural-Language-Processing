import csv


class IOOperations:


    def duygulariAyir(self, olumsuz=[], olumlu=[], notr=[]):
        with open('training.csv', encoding="utf8") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if(row[2] == 'Sad'):
                    olumsuz.append(row[2])
                elif(row[2] == 'Happy'):
                    olumlu.append(row[2])
                else:
                    notr.append(row[2])

    print("test")
