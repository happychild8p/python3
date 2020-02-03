#!/usr/bin/python3

employee_file = open("./created.txt", "w")

if employee_file.writable():
    employee_file.write("Toby - Human Resources")
    employee_file.write("\nKelly - Customer Service")

employee_file.close()
