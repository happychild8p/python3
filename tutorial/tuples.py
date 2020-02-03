#!/usr/bin/python3 


print("Tuples are immutable")
coordinates = (4, 5)

print(coordinates, coordinates[0], coordinates[1])

list1 = list(coordinates)

print(list1)

list1[1] = 7
print(list1)

list_of_tuples = [(4, 5), (6, 7), (80, 34)]

print(list_of_tuples)
