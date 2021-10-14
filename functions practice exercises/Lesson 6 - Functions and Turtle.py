
"""
import turtle
import random

def draw_circle(a_turtle, x, y, radius):
    a_turtle.color('red')
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()

    a_turtle.circle(radius)

def draw_filled_circle(a_turtle, x, y, radius):
    a_turtle.color('blue')
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()

def main( ):
    tula = turtle.Turtle()
    ryan = turtle.Turtle()
    draw_circle(tula, 100, 100, 50)
    draw_filled_circle(ryan, 200, 200, 50)


main()
turtle.done()
"""

import math
import turtle
import random

def draw_triangle(a_turtle, x, y, side_a, side_b):
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    angle_c = math.asin(side_b / side_c)
    c_deg = math.degrees(angle_c)
    other_ang = 180 - 90 - c_deg
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.setheading(90)
    a_turtle.forward(side_a)
    a_turtle.right(90)
    a_turtle.forward(side_b)
    a_turtle.right(180 - other_ang)
    a_turtle.forward(side_c)



def main():
    all_colours = ['dark sea green', 'coral', 'light salmon', 'sienna', 'dark sea green', 'blanched almond']

    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0,0,400,400)
    world.colormode(255)
    c = random.choice(all_colours)

    tula = turtle.Turtle()
    tula.width(5)
    tula.speed(10)

    tula.color(random.choice(all_colours))
    draw_triangle(tula, 100, 100, 200, 80)


main()
turtle.done()
"""
def draw_snowman(a_turtle, x, y):
    pass
"""

