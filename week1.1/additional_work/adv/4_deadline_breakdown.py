"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

import sys

minutes_remaining_input = input("Minutes remaining until the deadline: ")

# TODO: convert the input to an integer
minutes_remaining = int(minutes_remaining_input)

if minutes_remaining < 0:
    print("Input is negative.")
    sys.exit(1)

# TODO: calculate whole days, leftover hours, and remaining minutes
days = minutes_remaining // (24 * 60)
hours = minutes_remaining // 60 - days * 24
minutes = minutes_remaining - hours * 60 - days * 24 * 60

# TODO: print the breakdown using f-strings
print(f"Days: {days}\nHours: {hours}\nMinutes: {minutes}")

# Extension: detect negative values and print a warning instead
