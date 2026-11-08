# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

import sys

try:
    with open(sys.argv[1], "r") as f:
        magic, size, max_gray, *pixels = map(str.strip, f)
        if magic != "P2": raise ValueError

        width, height = map(int, size.split())
        max_gray = int(max_gray)
        pixels = [list(map(int, row.split())) for row in pixels if row]
        
    if len(pixels) != height:
        print("Invalid height")
    elif any(len(row) != width for row in pixels):
        print("Invalid width")
    elif any(not 0 <= pixel <= max_gray for row in pixels for pixel in row):
        print("Invalid pixel values")
    else:
        print("Valid image")
except IndexError:
    print("Error: Please provide a PGM filename.")
except FileNotFoundError:
    print(f"Error: Could not find {sys.argv[1]}.")
except (OSError, ValueError) as error:
    print(f"Error reading the PGM file: {error}")
