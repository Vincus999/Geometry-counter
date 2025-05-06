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
    # First step: count the semi-perimeter
    s = perimeter / 2
    # Second step: count the area with the semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Printing the perimeter of the triangle
    print(f"The perimeter of the triangle: {perimeter} ")
    print(f"The area of the triangle: {area} ")

    