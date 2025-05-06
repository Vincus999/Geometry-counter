


# Adding the value of the side "a"
a = float(input("Please give me the value of the cube's side (a): "))

# Checking the positivity of the given value
if a <= 0:
    print("Error: the given value is not positive. Please try again.")
else:
    # Counting the surface area
    surface_area = a * 6

    # Counting the volume
    volume = a ** 3

    # Printing the perimeter of the triangle
    print(f"The surface area of the cube: {surface_area} ")
    print(f"The volume of the cube: {volume} ")


