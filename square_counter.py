
# Adding the value of the side "a"
a = float(input("Please give me the value of the square's side (a): "))

# Checking the positivity of the given value
if a <= 0:
    print("Error: the given value is not positive. Please try again.")
else:
    # Counting the perimeter
    perimeter = a * 4

    # Counting the area
    area = a ** 2

    # Printing the perimeter of the triangle
    print(f"The perimeter of the square: {perimeter} ")
    print(f"The area of the square: {area} ")


