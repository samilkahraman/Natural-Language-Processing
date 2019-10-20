from IOOperations import IOOperations

olumlu =[]
olumsuz = []
notr = []

emp1 = IOOperations()
"This would create second object of Employee class"
emp2 = IOOperations()

emp1.duygulariAyir(olumlu, olumsuz, notr)
print(len(olumlu))
print(len(olumsuz))
print(len(notr))