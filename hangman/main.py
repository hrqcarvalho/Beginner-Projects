"""
First of all, I apologize for this being such a messy, but i thought it would be coller if i let all the comments
the dr. made in order to guide us through this challenge.
"""
from random import choice

word_list = ["dragonborn", "kenway", "luffy"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)
#TODO-1.1: - Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for each_letter in chosen_word:
    display.append("_")

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#TODO-3.1: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
index = -1
for each_letter in chosen_word:
    index += 1
    if guess == each_letter:
        display[index] = guess

#TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)
