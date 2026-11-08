# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.

# Hints:
# - Remember to add \n for new lines when writing to files

name = input("Enter your name: ")
age = input("Enter your age: ")
favourite_colour = input("Enter your favourite colour: ")

with open("user_info.txt", "w") as f:
    f.write(f"{name}\n{age}\n{favourite_colour}\n")

# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
