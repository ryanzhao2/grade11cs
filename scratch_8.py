import math

def area_circle( r ):
    area = (math.pi * (r ** 2))
    return area


def volume_sphere( r ):
    volume = ((4/3) * math.pi) * (r ** 3)
    return volume
#MAIN
radius = float(input("Enter a radius:"))

#call the area function
radius_circle = area_circle(radius)
print(f'The area of the circle is {radius_circle:.2f}')

#call the volume function
radius_sphere = volume_sphere(radius)
print(f'The volume of the sphere is {radius_sphere:.2f}')
#print the result