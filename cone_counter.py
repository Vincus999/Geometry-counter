





import math

# Adding the value of the radius
r = float(input("Please give me the value of the radius (r): "))
h = float(input("Please give me the value of the height (h): "))

# Checking the positivity of the given value
if r <= 0 or h <= 0:
    print("Error: the radius is not positive. Please try again.")
else:

    # Counting the surface area
    surface_area = h * math.pi * r  + math.pi ** 2

    # Counting the volume
    volume = (1 / 3) * math.pi * h *  r ** 2

    # Printing the volume and the surface area
    print(f"The surface area of the cone: {surface_area} ")
    print(f"The volume of the cone: {volume} ")

