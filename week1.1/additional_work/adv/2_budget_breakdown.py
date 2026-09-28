"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = input("Travel cost in pounds: ")
food_cost_input = input("Food cost in pounds: ")
accommodation_cost_input = input("Accommodation cost in pounds: ")

# TODO: convert each value to a number type that supports decimals
travel_cost = float(travel_cost_input)
food_cost = float(food_cost_input)
accommodation_cost = float(accommodation_cost_input)

# TODO: calculate the total and the average spend per category
total = travel_cost + food_cost + accommodation_cost

# TODO: print the three costs, the total, and the average
print(f"Travel: £{travel_cost:.2f}")
print(f"Food: £{food_cost:.2f}")
print(f"Accomodation: £{accommodation_cost:.2f}")
print(f"Total: £{total}")
print(f"Average: £{total / 3}")

# Extension: format the totals to two decimal places
