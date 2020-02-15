#!/usr/bin/python3

class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return self.first +' '+ self.last
   
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(Employee.num_of_emps)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.06 
print(Employee.__dict__)
emp_1.raise_amount = 1.10
print(emp_1.__dict__)
emp_1.apply_raise()
print(emp_1.pay)
