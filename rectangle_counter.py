

# Adding the value of the sides
a = float(input("Please give me the value of the rectangle's first side (a): "))
b = float(input("Please give me the value of the rectangle's second side (b): "))

# Checking the positivity of the given values
if a <= 0 or b <= 0:
    print("Error: the radius is not positive. Please try again.")
else:
    # Counting the perimeter
    perimeter = 2 * (a + b)

    # Counting the area
    area = a * b

    # Printing the perimeter of the triangle
    print(f"The perimeter of the rectangle: {perimeter} ")
    print(f"The area of the rectangle: {area} ")

