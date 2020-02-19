#!/usr/bin/python3

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first +' '+ self.last
    
    def apply_raise(self):
        self.pay = int(self.pay * raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self. fullname())

emp_1 = Employee('Corey', 'Schafer', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(len(emp_1))
print(emp_1.__len__())
print(emp_1 + emp_2)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

