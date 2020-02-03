#!/usr/bin/python3

monthConversion = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

print(monthConversion)
print("\n")
print(monthConversion[10])
print("\n")
print(monthConversion.keys())
print("\n")
print(monthConversion.values())
print("\n")
print(monthConversion.get(5))
print("\n")
print("get(key,default value): "+monthConversion.get(15, "Invalid month"))
