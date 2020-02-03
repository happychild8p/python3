#!/usr/bin/python3

employee_file = open("./test.txt", "r")

if employee_file.readable():
    print(employee_file.read())
    employee_file.seek(0)
    print(employee_file.readline())
    employee_file.seek(0)
    print(employee_file.readlines())
    employee_file.seek(0)

employee_file.close()
