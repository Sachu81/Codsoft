#PASSWORD GENARATOR

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
           , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

character = ['!', '@', '#', '$', '%', '&', '*', '+', ':', '<', '>', '/', '(', ')']

# Give The Input From User
numbers_letters = int(input("Enter The Number of letters Do You want:"))

numbers_number = int(input("Enter The Numbers of number Do You want:"))

numbers_character = int(input("Enter The Number of letters Do You want:"))

#GENERATE PASSWORD

password =""

for char in range(1, numbers_letters+1):
    password += random.choice(letters)

for char in range(1, numbers_number+1):
    password += random.choice(number)

for char in range(1, numbers_character+1):
    password += random.choice(character)



