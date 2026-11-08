# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"
import sys

try:
    with open(sys.argv[1], "r") as f:
        magic, size, max_gray, *pixels = map(str.strip, f)
        if magic != "P2": raise ValueError

        width, height = map(int, size.split())
        max_gray = int(max_gray)
        pixels = [list(map(int, row.split())) for row in pixels if row]
        inverted = [[max_gray - pixel for pixel in row] for row in pixels]

    with open("inverted.pgm", "w") as f:
        f.write(f"P2\n{width} {height}\n{max_gray}\n")
        f.writelines(" ".join(map(str, row)) + "\n" for row in inverted)

except IndexError:
    print("Error: Please provide a PGM filename.")
except FileNotFoundError:
    print(f"Error: Could not find {sys.argv[1]}.")
except (OSError, ValueError) as error:
    print(f"Error processing the PGM file: {error}")
