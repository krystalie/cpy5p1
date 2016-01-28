# q2_calc_cylinder_volume.py
# Calculate cylinder volume

import math

# input radius
radius = float(input("Enter radius: "))

# input length
length = float(input("Enter length: "))

# compute area
area = radius * radius * math.pi

# compute volume
volume = area * length

# output volume
print("Cylinder volume =", volume)
