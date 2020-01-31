#!/usr/bin/python3

print("Giraffe\nAcademy")
print("\ is a special escape character which make preceeding character to be escaped from being string character")
print("For example \ + n will be treated as new line character.")

phrase = "Giraffe Academy"


print(phrase+" is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print("\n"+phrase+" has "+str(len(phrase))+" characters.")
print("\nI want to access to a specific character in string,")
print(phrase[0]+phrase[1]+phrase[2]+phrase[3]+phrase[4]+phrase[5])
print("It starts from 0 index")
print("\nFind index number of specific character")
print("Index # of 'A' is "+str(phrase.index("A")))
print("Index # of 'a' is "+str(phrase.index("a")))
print("\n"+phrase+" has the rival: "+phrase.replace("Giraffe", "Elephant"))
