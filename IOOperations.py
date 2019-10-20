import csv


class IOOperations:

    empCount = 0
    olumlu = []
    olumsuz = []
    notr = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        IOOperations.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % IOOperations.empCount)

    def displayEmployee(self):
        print  ("Name : ", self.name, ", Salary: ", self.salary)

    with open('training.csv', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(row[2] == 'Sad'):
                olumsuz.append(row[2])
            elif(row[2] == 'Happy'):
                olumlu.append(row[2])
            else:
                notr.append(row[2])
        print(len(olumlu))
        print(len(olumsuz))
        print(len(notr))

