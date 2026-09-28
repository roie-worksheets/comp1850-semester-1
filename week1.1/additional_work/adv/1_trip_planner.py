"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

# TODO: convert distance_miles_input and time_hours_input to numbers
distance_miles = float(distance_miles_input)
time_hours = float(time_hours_input)

# TODO: calculate the average speed in miles per hour
average = distance_miles / time_hours

# TODO: print a summary message using an f-string
print(f"The average for {destination} is {average:.2f}")
# Extension: add validation for zero or negative values
