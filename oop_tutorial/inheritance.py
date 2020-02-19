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
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->"+emp.fullname())

emp_1 = Employee('Corey', 'Schafer', 60000)
dev_1 = Developer('Test', 'User', 50000, 'Python')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

#print(help(Developer))
#print(dev_2)

print(mgr_1.email)
mgr_1.add_emp(emp_1)
mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
print("=================")
mgr_1.print_emp()

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay, dev_1.prog_lang)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
#print(dev_1.fullname())
#print(Employee.fullname(dev_1))
