#!/usr/bin/python3

jumin = "950601-1023121"
gender = jumin[7]
print(gender)

my_array = ['Python','is','a','language']
for i in my_array:
    print(i, end=' ')
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

sum = 0
for i in range(1, 101):
    if i % 5 == 0:
		    sum = sum + i
print(sum)

import math

def my_max(a, b):
		if a > b:
				return a
		elif a < b:
				return b
		else:
				return "Both variables have same value {}".format(a)

def my_abs(val):
		return abs(val)

def my_abs2(val):
		if val >= 0:
				return val
		else:
				return val*-1

def dis(x1, y1, x2, y2):
		width = my_abs2(x2 - x1)
		length = my_abs2(y2 - y1)
		vector = math.sqrt(width**2 + length**2)
		return vector

if __name__ == "__main__":
		print(my_max(2, 2))
		print(my_abs(-7))
		print(my_abs2(-81))
		print(dis(1,-13,6,-1))
