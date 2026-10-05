# Worksheet 1.2: Task 2 Solution
from sys import exit

from util import read_numbers

values = read_numbers()

if len(values) == 0:
    exit("Error: no numbers provided")

print(f"Minimum = {min(values)}")
print(f"Maximum = {max(values)}")
print(f"Mean = {sum(values) / len(values)}")
print(f"Median = {(mid := len(values) // 2, sorted(values)[mid] if len(values) % 2 == 1 else sum(sorted(values)[mid - 1:mid + 1]) / 2)[1]}")

        