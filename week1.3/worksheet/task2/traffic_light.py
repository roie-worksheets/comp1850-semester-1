"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
maxtime = int(input())  # read an integer number of steps (>0)
state = "red"

# Simulate the traffic light system up to time=maxtime in 1-second steps

max_count = states[state]
count = 0

for i in range(maxtime + 1):
    print(f"Time {i:03} State {state}")
    count += 1

    if count >= max_count:
        state = list(states.keys())[(list(states.keys()).index(state) + 1) % len(states)]
        max_count = states[state]
        count = 0
        
# At the end of each step you should output the time and state using the statement on line 14