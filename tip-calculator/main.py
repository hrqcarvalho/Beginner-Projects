"""
 A program that takes a value, tip's percentage
and a number of people and return the splitted bill.
"""

print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = (int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100 + 1)
n_people = int(input("How many people to split the bill? "))

total = bill * tip / n_people

print(f"Each person should pay: ${total:.2f}")
