#!/usr/bin/python3

from Student import Student

student1 = Student("Oscar", "Accountant", 3.1, False)
student2 = Student("Tom", "Biology", 4.0, False)

print(student1.name, student1.gpa, student1.major)
print(student2.name, student2.gpa, student2.major)

print(student1.honor_roll())
print(student2.honor_roll())
