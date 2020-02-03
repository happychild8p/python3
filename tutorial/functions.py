#!/usr/bin/python3

def say_hi():
    name = input("What is your name? ")
    print("Hello "+name)

def say_hi_with_parameter(name, age):
    print("Hello "+name+ ", you are "+age)
    
def say_hi_with_return(name):
    return "Hello "+name+" finish your tutorial ASAP!!"

print("Before function to be called.")
say_hi()
print("After function")
try:
    print(name)
except:
    print("There is no variables called 'name' outside the function")

print("2nd function with parameter")
say_hi_with_parameter("Heedong", "26")

print("3rd function")
print(say_hi_with_return("Heedong"))

