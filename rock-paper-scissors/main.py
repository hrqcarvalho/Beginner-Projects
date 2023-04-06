"""
A program that takes three possible inputs (0, 1 or 2) and simulate a rock paper scissors 
game.
"""
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# All the starting setup
plays = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors!")

# Player turn
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Pc turn
pc_choice = randint(0, 2)

# Result processing
if 0 <= player_choice < 3: 

    if player_choice == pc_choice:
        result = "It's a draw."
    elif player_choice == 0 and pc_choice == 2:
        result = "You win!"
    elif player_choice == 2 and pc_choice == 0:
        result = "You lose."
    elif player_choice > pc_choice:
        result = "You win!"
    else:
        result = "You lose."

    # Display
    print(f"\n{plays[player_choice]}")
    print("Computer chose:")
    print(f"\n{plays[pc_choice]}")
    print(result)

else:
    print("You typed an invalid number, you lose.")
