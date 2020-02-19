#!/usr/bin/python3

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property    
    def email(self):
        return self.first + '.' + self.last + '@company.com'
    
    @property 
    def fullname(self):
        return self.first +' '+ self.last
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

emp_1 = Employee('Corey', 'Schafer')
emp_2 = Employee('Test', 'User')

emp_1.first = 'Jim'

emp_1.fullname = 'Lesomam Scahfer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
