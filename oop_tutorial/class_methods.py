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
    
    @classmethod #altering the functionality of the method
    def set_raise_amt(cls, amount):
         cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

emp_str_1 = 'John-Doe-60000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)

print(emp_3.fullname())
print(emp_4.pay)
print(emp_5.email)
