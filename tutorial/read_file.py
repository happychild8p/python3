#!/usr/bin/python3

f = open("phone.txt","r")
lines = f.read()
print(lines)
f.close()

f = open("phone.txt", "r")
line = f.readlines()
print(line)
f.close()

print("\nAAAAAAAAAAAAAAAAAA\n")
f = open("phone.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    print(line)
f.close()

print("\nThis also works\n")
f = open("phone.txt", "r")
for line in f:
    line = line.rstrip()
    print(line)


for line in infile:
    line = line.rstrip().split()
