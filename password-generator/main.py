"""
A program that takes what do you want in your password (how many letters, numbers and symbols) 
and make a "random" password out of it.
"""
from random import choice, shuffle

# I'm using for loops here and not the libs because I think that's the point of this
# project.

print("Welcome to the Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like in your password?\n"))
numbers_count = int(input("How many numbers would you like in your password?\n"))

result = []
for letter in range(letters_count):
    result.append(choice(letters))

for symbol in range(symbols_count):
    result.append(choice(symbols))

for number in range(numbers_count):
    result += choice(numbers)

shuffle(result)
print(f"Here is your password: {''.join(result)}")
