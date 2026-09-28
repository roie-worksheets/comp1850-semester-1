"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
savings = input("How much would you like to save per month? ")

while True:
    try:
        savings = int(savings)
        break
    except ValueError:
        print("Invalid amount")
        savings = input("How much would you like to save per month? ")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
print(f"You will have saved {savings * 12} by the end of the year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
print(f"Total amount will be £{(savings * 12) * 1.008:.2f}")