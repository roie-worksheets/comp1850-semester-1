# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)
import sys
 
try:
    with open(sys.argv[1], "r") as f:
        magic, size, max_gray, *pixels = map(str.strip, f)
        if magic != "P2": raise ValueError

        width, height = map(int, size.split(' '))
        max_gray = int(max_gray)

    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Gray Value: {max_gray}")

except FileNotFoundError:
    print(f"Error: Could not find {sys.argv[1]}.")
except (OSError, ValueError, StopIteration) as error:
    print(f"Error reading the PGM file: {error}")
