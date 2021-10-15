#RYAN ZHAO
#OCTOBER 15, 2021
#LESSON #5

#QUESTION #1
"""
import math

def hypotenuse(a, b):
   h = math.sqrt(a ** 2 + b ** 2)
   return h

#MAIN
side_1 = float(input("Enter one side of the triangle"))
side_2 = float(input("Enter another side of the triangle"))

hyp = hypotenuse(side_1, side_2)
print(f'The hypotenuse of your triangle is {hyp:.1f}')
"""

#QUESTION #2
"""
def convert_to_fah(c_temp):
   f = ((9 / 5) * c_temp + 32)
   return f


#MAIN
celcius = float(input("Please enter temperature in Celcius"))
fahrenheit = convert_to_fah(celcius)

print(f'Temp in Celcius: {celcius:.0f}')
print(f'Temp in Fahren: {fahrenheit:.0f}')
"""

#QUESTION #3
"""
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
"""

#QUESTION #4
"""
def is_even(num):
   if num % 2 == 0:
      return True


#MAIN

user_num = int(input("Please enter a number"))

if is_even(user_num) == True:
    print(f'{user_num} is even')

else:
    print(f'{user_num} is odd')
"""

#QUESTION #5
"""
def calculate_tax(price):
   tax = price * 0.13
   return tax


# MAIN
user_price = 109.99
tax_amount = calculate_tax(user_price)
print(f'The tax of $109.99 is {tax_amount}')
"""

#QUESTION #6
"""
def boxname(name):
    s = '*' * (len(name) + 2) + '\n'
    s += f'*{name}*\n'
    s += '*' * (len(name) + 2) + '\n'
    return s

my_name = input("Enter your name")
box = boxname(my_name)
print(f'{box}')
"""

#QUESTION #7
"""
def clear_screen():
    for i in range(25):
        print('\n')
clear_screen()
"""

#QUESTION #8
"""
def is_leap_year(some_year):
    if (some_year % 4 == 0 and some_year % 100 != 0 or some_year % 400 == 0):
        return True
    return False


user_year = int(input("Enter a number: "))
leap_year = is_leap_year(user_year)
print(f'{leap_year}')
"""
