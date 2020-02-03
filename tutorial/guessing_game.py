#!/usr/bin/python3

secret_word = "serotonin"
guess = ""
counter = 0
limit = 5
fail = False

while guess != secret_word and not(fail):
    if counter < limit:
        guess = input("Enter your guess: ")
        counter = counter + 1
    else:
        fail = True

if fail:
    print("Out of guesses, YOU HAVE LOST")
else:
    print("You have won!")
