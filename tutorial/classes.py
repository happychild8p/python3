#!/usr/bin/python3

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Anna", "Electronic Engineering", 2.8, False)
student3 = Student("Pam", "Art", 2.5, True)

print(student1.gpa, student1.name)
print(student2.gpa, student2.is_on_probation)

