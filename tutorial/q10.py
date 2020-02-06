#!/usr/bin/python3

num1 = int(input("First integer number: "))
num2 = int(input("Second integer number: "))
result = num1 + num2
print(str(num1)+"+"+str(num2)+"="+str(result))

while (result >= 10):

	num1 = int(str(result)[0])
	num2 = int(str(result)[1])

	result = num1 + num2
	
	print(str(num1)+"+"+str(num2)+"="+ str(result))

#print("Final result is : "+str(result))
    

