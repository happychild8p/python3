#!/usr/bin/python3

lucky_numbers = [4, 1, 15, 16, 2, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(lucky_numbers, friends)

friends.extend(lucky_numbers)
print("\nextend(list/or value): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.append("Harry")
print("\nappend(): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.insert(2,"Kelly")
print("\ninsert(index, value): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.remove("Jim")
print("\nremove(value): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.clear()
print("\nclear(): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.pop()
print("\npop(): "+str(friends))
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print("\nindex(Jim): "+str(friends.index("Oscar")))
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print("\ncount(Jim): "+str(friends.count("Jim")))

print(lucky_numbers)
lucky_numbers.sort()
print("sort(): "+str(lucky_numbers))

lucky_numbers.reverse()
print("reverse(): "+str(lucky_numbers))

friends2 = friends.copy()
print("copy(): "+ str(friends2))
