"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
cleaned_message = raw_message.strip().title()

# TODO: display the original and cleaned messages
print(f"Original: {raw_message}\nCleaned: {cleaned_message}")

# Extension: display the character counts for each version
print(f"Original count: {len(raw_message)}\nCleaned count: {len(cleaned_message)}")