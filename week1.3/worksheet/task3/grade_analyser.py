# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

# open the file

# read in the data, and for each student calculate their average grade and classification

import csv

input_filename = input("Enter the student filename: ")
output_filename = input_filename + "_out.csv"

try:
    with open(input_filename, "r") as _in, open(output_filename, "w") as _out:
        reader, writer = csv.reader(_in), csv.writer(_out)
        next(reader, None)

        for row in reader:
            if not row: continue
            student_id = row[0]
            
            grades = [int(grade) for grade in row[1:] if grade.strip()]
            if not grades: continue

            average = sum(grades) / len(grades)

            if average >= 70:
                classification = "1"
            elif average >= 60:
                classification = "2:1"
            elif average >= 50:
                classification = "2:2"
            elif average >= 40:
                classification = "3"
            else:
                classification = "F"

            writer.writerow([student_id, f"{average:.2f}", classification])
    print(f"Results written to {output_filename}")
except FileNotFoundError:
    print(f"Error: Could not find {input_filename}.")
except (OSError, ValueError) as error:
    print(f"Error processing the file: {error}")


# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder
