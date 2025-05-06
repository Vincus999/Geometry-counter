
import math

# Adding the value of the radius
r = float(input("Please give me the value of the radius (r): "))

# Checking the positivity of the given value
if r <= 0:
    print("Error: the radius is not positive. Please try again.")
else:

    # Counting the perimeter
    perimeter = 2 * math.pi * r

    # Counting the area
    area = math.pi * r ** 2

    # Printing the perimeter of the triangle
    print(f"The perimeter of the circle: {perimeter} ")
    print(f"The area of the circle: {area} ")
