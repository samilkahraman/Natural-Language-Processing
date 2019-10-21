from IOOperations import IOOperations

olumlu =[]
olumsuz = []
notr = []

emp1 = IOOperations()
"This would create second object of Employee class"
emp2 = IOOperations()

emp1.duygulariAyir(olumsuz,olumlu, notr)

emp1.yorumlariCsvlereAktar("olumluYorumlar.csv", olumlu)
emp1.yorumlariCsvlereAktar("olumsuzYorumlar.csv", olumsuz)
emp1.yorumlariCsvlereAktar("notrYorumlar.csv", notr)
print(olumsuz[2])