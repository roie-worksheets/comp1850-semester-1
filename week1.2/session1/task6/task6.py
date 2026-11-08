
# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database: artist names mapped to lists of album names
music = {
    "Fleetwood Mac": [
        {"name": "Rumours", "year": 1977},
        {"name": "Tusk", "year": 1979}
    ],
    "Björk": [
        {"name": "Debut", "year": 1993},
        {"name": "Homogenic", "year": 1997}
    ]
}

# Pretty-print the data structure
pprint(music)

# Display the first album recorded by a specific artist
print(music["Fleetwood Mac"][0])

