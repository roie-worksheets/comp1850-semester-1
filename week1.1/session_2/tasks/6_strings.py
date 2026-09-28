# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")  # original
print(f"Modified String 1: {user_string.lower()}")  # lowercase
print(f"Modified String 2: {user_string.upper()}")  # uppercase
print(f"Modified String 3: {user_string.strip()}")  # remove leading and trailing whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}")  # replaces lowercase a with @
print(f"Modified String 5: {user_string.capitalize()}")  # capitalizes the first letter of the string
print(f"Modified String 6: {user_string[::-1]}")  # reverse
print(f"Modified String 7: {user_string.title()}") # titlecases each word in a string
print(f"Modified String 8: {len(user_string)}") # returns the length of the string
print(f"Modified String 9: {user_string.find('a')}") # finds the first index where lowercase a appears
print(f"Modified String 10: {user_string.count('a')}") # returns the number of occurences of lowercase a
print(f"Modified String 11: {user_string.startswith('Hello')}") # returns whether the string starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}") # returns whether the string ends with !
print(f"Modified String 13: {user_string.isalnum()}") # returns whether the string consists entirely of alphanumeric characters
print(f"Modified String 14: {user_string.isalpha()}") # returns whether the string consists entirely of alphabetic characters
print(f"Modified String 15: {user_string.isdigit()}") # returns whether the string consists entirely of numeric characters


######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!
