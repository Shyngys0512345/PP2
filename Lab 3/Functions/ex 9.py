import math


def sphere_volume(radius):
    return 4 / 3 * math.pi * math.pow(radius, 3)

radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print("The volume of the sphere with radius", radius, "is", volume)