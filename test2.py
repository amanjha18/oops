class Employee:
    increment = 1.5
    no_of_Employee = 0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname =lname
        self.salary = salary
        Employee.no_of_Employee +=1

    def increase(self):
        self.salary = int(self.salary *Employee.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount 

harry=Employee('harry', 'jackson', 44000)
rohan = Employee('rohan', 'das', 44000)
Employee.change_increment(4)
'''
print(harry.salary)
harry.increase()
print(harry.salary)
print(Employee.no_of_Employee)
'''
class programmer(Employee):
    pass
harry=programmer('harry', 'jackson', 99000)
print (harry.fname, harry.lname)
