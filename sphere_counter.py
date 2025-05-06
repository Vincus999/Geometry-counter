


import math

# Adding the value of the radius
r = float(input("Please give me the value of the radius (r): "))

# Checking the positivity of the given value
if r <= 0:
    print("Error: the radius is not positive. Please try again.")
else:

    # Counting the surface area
    surface_area = 4 * math.pi * r ** 2

    # Counting the volume
    volume = (4 / 3) * math.pi * r ** 3

    # Printing the perimeter of the triangle
    print(f"The perimeter of the circle: {surface_area} ")
    print(f"The area of the circle: {volume} ")

