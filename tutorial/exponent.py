#!/usr/bin/python3

def raise_to_power(base, exponent):
    result = 1

    for index in range(1, (exponent + 1)):
        result = result * base
    return result

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

print(raise_to_power(base, exponent))
