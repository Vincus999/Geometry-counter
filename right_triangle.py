
import math

# Adding the value of the sides
a = float(input("Please give me the value of the triangle's first side (a): "))
b = float(input("Please give me the value of the triangle's second side (b): "))
c = float(input("Please give me the value of the triangle's third side (c): "))


# Checking the positivity of the given values
if a <= 0 or b <= 0 or c <= 0:
    print("Error: one of the given values are not positive. Please try again.")
else:
    # Counting the perimeter
    perimeter = a + b + c

    # Counting the area
    area = (a * b) / 2

    # Printing the perimeter of the triangle
    print(f"The perimeter of the ight angle triangle: {perimeter} ")
    print(f"The area of the right angle triangle: {area} ")

