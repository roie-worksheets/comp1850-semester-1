# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
import csv

try:
    with open("student_data.csv") as file:
        data = list(csv.reader(file))

    with open("report.txt", "w") as report:
        for row in data[1:]:
            name = row[1]
            maths, science, history = map(int, row[2:5])
            average = (maths + science + history) / 3
            report.write(f"{name}: {average:.2f}\n")
except FileNotFoundError as error:
    print(f"Error: Could not find {error.filename}.")
except (ValueError, IndexError) as error:
    print(f"Error processing student data: {error}")
