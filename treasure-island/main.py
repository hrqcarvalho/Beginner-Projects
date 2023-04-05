"""
A program that tells a short story (the point here is to test the knowledge about 
if-else statements
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.\n")

print("You are in a island looking for a treasure, feeling like Indiana Jones and then you\
 reach your first challenge:")
print("You are on a narrow bridge and a huge round rock comes in your direction.")
rock_challenge = input(
    "You have to dodge it, which side do you choose? ['Left' or 'Right']? ").lower()

if rock_challenge == 'left':
    print("\nYou dodge it to the left, fall but hold on to a vine.")
    print("Under you there is a river full of crocodiles.")

    river_challenge = input(
        "What do you do now? Keep holding or swim? ['Swim' or 'Hold']? ").lower()

    if river_challenge == 'hold':
        print("\nYou keep holding and then you see an entry of a cave in a mountain.")
        print("You get all 'Tarzan' and manage to get there safely.")

        door_challenge = input(
            "Inside the cave you see three doors, which one do you open? ['Red', 'Yellow' or 'Blue']? ").lower()

        if door_challenge == "yellow":
            print("\nSomehow you did it! You found the Legendary Ancient Treasure!")
        else:
            print("\nYou open the door and there is an entire army of undead warriors.")
            print("You are dead.")
            print("Game Over.")
    else:
        print("\nYou push your luck and it fails, you are eaten.")
        print("Game Over.")
else:
    print("\nYou dodge it to the right, fall and land right in front of a crocodile.")
    print("You are pretty much dead.")
    print("Game Over.")
