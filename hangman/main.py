"""
First of all, I apologize for this being such a messy, but i thought it would be coller if i let all the comments
the dr. made in order to guide us through this challenge.

This program it's a digital version of the famous game "Hangman", so you know the rules, guess a letter if you got it
 right fill a blank otherwise you lose a life
"""
from random import choice
from hangman_art import *
from hangman_words import word_list

#TODO-0: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-0.1: - Import the logo from hangman_art.py and print it at the start of the game.
lives = 6
print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = choice(word_list)
#TODO-1.1: - Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for _ in chosen_word:
    display.append("_")

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-2.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters 
# in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#TODO-2.2: - If the user has entered a letter they've already guessed, print the letter and let them know.
while '_' in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #TODO-3.1: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    #TODO-3.2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess in chosen_word:
        index = -1
        for each_letter in chosen_word:
            index += 1
            if guess == each_letter:
                display[index] = guess
    else:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(stages[0])
            print("You lose.")
            break

    #TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Join all the elements in the list and turn it into a String.
    #TODO-4.1: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(f"{' '.join(display)}")
    print(stages[lives])

else:
    print("You win!")
