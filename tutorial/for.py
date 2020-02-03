#!/usr/bin/python3 

friends = ["Jim", "Karen", "Kevin", "Harry"]
for name in friends:
    print(name)

for index in range(4, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index - 1])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not the first iteration")
