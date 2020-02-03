#!/usr/bin/python3

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
	print("You are a small male")
elif not(is_male) and is_tall:
    print("You are tall")
else:
    print("You are neither a male nor tall")

