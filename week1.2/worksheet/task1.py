# Worksheet 1.2: Task 1 Solution
from sys import exit


def get_number(text):
    try:
        return int(input(text))
    except ValueError:
        exit("Error: Grade must be an integer between 0 and 100")
        
grade = get_number("Enter the grade: ")

if 0 <= grade <= 39:
    print(f"{grade} is a Fail")
elif 40 <= grade <= 69:
    print(f"{grade} is a Pass")
elif grade > 100 or grade < 0:
    exit("Error: Grade must be an integer between 0 and 100")
else:
    print(f"{grade} is a Distinction")