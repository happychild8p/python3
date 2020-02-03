#!/usr/bin/python3

try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = float(numerator / denominator)
    print(str(numerator)+" / "+str(denominator)+" = "+str(result))

except ValueError:
    print("You haven't entered a number. Invalid Input")
except ZeroDivisionError as err:
    print("Denominator cannot be 0 dude. Did you drop out from kindergarten?")
    print(err)
