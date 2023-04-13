"""
This project is a little different because this time I need to go to a website 
to code a script which will be used to help a bot to escape a maze.
"""

# Ignore these non-sense functions they only make sense in that site. 
def turn_left():
    pass

def move():
    pass

def wall_on_right():
    pass

def front_is_clear():
    pass

def at_goal():
    pass

def right_is_clear():
    pass

# My solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

if not wall_on_right():
    while front_is_clear():
        move()
    turn_left()
   
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()
