"""
import turtle
import random
import math


def draw_circle(a_turtle, x, y, radius):
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()

    a_turtle.setheading(0)
    a_turtle.circle(radius)


def draw_triangle(a_turtle, x, y, a, b):
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()

    a_turtle.setheading(random.randrange(0, 360, 30))
    a_turtle.forward(a)
    a_turtle.right(90)
    a_turtle.forward(b)

    c = math.sqrt(a ** 2 + b ** 2)
    angle = 180 - math.degrees(math.asin(a / c))

    a_turtle.right(angle)
    a_turtle.forward(c)


def draw_rect(a_turtle, x, y, width, height):
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)


def draw_user_shape(a_turtle, user_shape_choice):
    x = random.randint(0, 300)
    y = random.randint(0, 300)

    if user_shape_choice == "rectangle":

        draw_rect(a_turtle, x, y, \
                  random.randrange(50, 201, 50), \
                  random.randrange(50, 201, 50))

    elif user_shape_choice == "circle":

        draw_circle(a_turtle, x, y, \
                    random.randrange(20, 201, 20))

    elif user_shape_choice == "triangle":

        draw_triangle(a_turtle, x, y, \
                      random.randrange(50, 201, 50), \
                      random.randrange(50, 201, 50))

    else:

        a_turtle.up()
        a_turtle.goto(x, y)
        a_turtle.down()
        a_turtle.write("Sorry, I don't know that shape")


def main():
    all_colours = ["tan", "light steel blue", "midnight blue", "indian red", "peru"]

    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0, 0, 400, 400)
    world.bgcolor(random.choice(all_colours))

    tula = turtle.Turtle()
    tula.speed(10)
    tula.width(5)

    tula.color(random.choice(all_colours))
    user_choice = world.textinput("Which Shape", "Which shape would you like: \n\ncircle, rectangle, triangle?\n")
    draw_user_shape(tula, user_choice)

main()
turtle.done()
"""
"""
import turtle
import random
global tula

def draw_dots(mouse_x, mouse_y):
    global tula

    if mouse_y >= 0 and mouse_y < 100:
        val = 35
        tula.color('red')
    elif mouse_y > 100 and mouse_y < 200:
        val = 20
        tula.color('orange')
    elif mouse_y > 200 and mouse_y < 300:
        val = 15
        tula.color('sandy brown')
    else:
        val = 5
        tula.color('bisque')

    tula.up()
    tula.goto(mouse_x, mouse_y)
    tula.down()
    tula.dot(val)

def get_random_colour():

    c = (random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255))

    return c

def main():
    global tula
    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0, 0, 400, 400)
    world.colormode(255)
    c = get_random_colour()
    world.bgcolor(c)
    tula = turtle.Turtle()
    tula.speed(10)

    world.onclick(draw_dots)


main()
turtle.done()

"""
import turtle
import random


def race(tula, henrietta):
    for i in range(80):
        walk_random(tula)
        walk_random(henrietta)


    #check_who_won(tula, henrietta)


def create_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.width(1)
    new_turtle.speed(1)
    c = (random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255))
    new_turtle.color(c)
    return new_turtle


def start(a_turtle):
    a_turtle.up()
    a_turtle.goto(200, 0)
    a_turtle.down()


def walk_random(a_turtle):
    a_turtle.setheading(random.randint(0, 180))
    a_turtle.forward(random.randint(0, 20))


def world_setup():
    world = turtle.Screen()
    world.setup(width=400, height=400)
    world.setworldcoordinates(0, 0, 400, 400)
    world.colormode(255)
    c = (random.randint(0, 255), \
         random.randint(0, 255), \
         random.randint(0, 255))
    world.bgcolor(c)
    return world


def main():
    world = world_setup()

    tula = create_turtle()
    henrietta = create_turtle()

    start(tula)
    start(henrietta)

    race(tula, henrietta)


main()
turtle.done()