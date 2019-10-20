from IOOperations import IOOperations


b = "Hello, World!"
print(b[2:5])

"This would create first object of Employee class"
emp1 = IOOperations("Zara", 2000)
"This would create second object of Employee class"
emp2 = IOOperations("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % IOOperations.empCount)