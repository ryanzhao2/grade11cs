#RYAN ZHAO
#OCTOBER 15, 2021
#LESSON #6

#QUESTION #1
"""
import turtle
import random

def world_setup():
    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0, 0, 400, 400)
    return world

def draw_circle(a_turtle, x, y, radius, mycolor):
    a_turtle.color(mycolor)
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()

    a_turtle.circle(radius)

def draw_filled_circle_with_color(a_turtle, x, y, radius, mycolor):
    a_turtle.color(mycolor)
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()

def main( ):
    world = world_setup()
    tula = turtle.Turtle()
    ryan = turtle.Turtle()
    draw_circle(tula, 100, 100, 50, 'red')
    draw_circle(tula, 50, 50, 30, 'orange')
    draw_filled_circle_with_color(ryan, 300, 50, 70, 'blue')
    draw_filled_circle_with_color(ryan, 200, 80, 10, 'green')


main()
turtle.done()
"""

#QUESTION #2
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

#QUESTION #3
"""
import turtle
import random

def motion(event):
    x, y = event.x, event.y
    print(f'{x}, {600-y}')
canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)

def world_setup():
    world = turtle.Screen()
    world.setup(width=600, height=600)
    world.setworldcoordinates(0, 0, 600, 600)
    world.colormode(255)
    c = (223,149,149)
    world.bgcolor(c)
    return world


def draw_filled_circle_with_color(a_turtle, x, y, radius, mycolor):
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.color(mycolor)
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def main( ):
    world = world_setup()
    ryan = turtle.Turtle()
    draw_filled_circle_with_color(ryan, 300, 200, 50, 'white')
    draw_filled_circle_with_color(ryan, 300, 290, 35, 'white')
    draw_filled_circle_with_color(ryan, 300, 355, 25, 'white')
    draw_filled_circle_with_color(ryan, 300, 305, 5, 'black')
    draw_filled_circle_with_color(ryan, 300, 320, 5, 'black')
    draw_filled_circle_with_color(ryan, 300, 335, 5, 'black')
    draw_filled_circle_with_color(ryan, 290, 376, 7, 'black')
    draw_filled_circle_with_color(ryan, 310, 376, 7, 'black')





main()
turtle.done()
"""