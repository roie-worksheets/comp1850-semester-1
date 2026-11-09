# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_date(day, month, year, separator="-"):
    return f"{day}{separator}{month}{separator}{year}"


# Write code to test the function with separators such as "/", ":", "."
print(format_date(9, 11, 2026))       # 9-11-2026
print(format_date(9, 11, 2026, "/"))  # 9/11/2026
print(format_date(9, 11, 2026, ":"))  # 9:11:2026
print(format_date(9, 11, 2026, "."))  # 9.11.2026