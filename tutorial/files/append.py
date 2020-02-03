#!/usr/bin/python3

employee_file = open("./test_copy.txt", "a")

if employee_file.writable():
    employee_file.write("Toby - Human Resources")
    employee_file.write("\nKelly - Customer Service")

employee_file.close()
