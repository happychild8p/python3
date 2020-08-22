#!/usr/bin/python3
word= input("Enter the answer: ")
wordlist = []; blank = []
for i in range(len(word)):
    wordlist.append(word[i])
    blank.append("_")

for j in range(10):
    guess = input("Guess a word: ")
    if guess not in wordlist: print("Wrong Answer!!\nYou have",9-j,"chance")
    else:
        for k in range(len(wordlist)):
            if guess == wordlist[k]:
                blank[k] = guess
                print("".join(blank),"\nYou have",9-j,"chance")
    if "_" not in blank: 
        print("You win!")
        break
