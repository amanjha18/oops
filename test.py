# learning class and objects

#__init__ is a initialiser or method.

class Employee: # class is like a template
    empCount = 0 #class variable
    def __init__(self,name,salary):# name and salary are argument of method.
        self.name=name #name is a class variable 
        self.salary=salary
        Employee.empCount+=1
    
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        (print "Name: ",self.name, " salary: ", self.salary)
emp1=Employee("aman", 100000)
emp2=Employee("yogendra",100000)
print emp1.displayEmployee()
print emp2.displayEmployee()
print "Total Employee %d" % Employee.empCout"
'''

class Student:
    def __init__(self, names, Address, Mnumber): # __init__ is a initializer.
        self.name=names # names is argument of class method and name is class varible
        self.Address=Address
        self.Mnumber=Mnumber
aman=Student('amanjha', 'noida', 9870543210)
aijaj=Student('aijajkhan', 'delhi', 1234560789)
print(aman.name,aman.Address, aman.Mnumber)
print(aijaj.name,aijaj.Address,aijaj.Mnumber)
'''


