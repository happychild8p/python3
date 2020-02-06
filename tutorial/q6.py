#!/usr/bin/python3

import math

number = int(input("Enter a number: "))
power = math.log(number,3)

if(math.ceil(power) == math.floor(power)):
    print(str(number)+" is the "+str(power)+" power of 3")
else:
    print(str(number)+" is not power of 3")
