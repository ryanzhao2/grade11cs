import turtle
def draw2lines(length, angle):
    alex.forward(length - 4)
    alex.right(angle)
    alex.forward(length - 4)
    alex.right(angle)

def drawHexagon(length, angle):

    alex.right(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)
    alex.right(angle)


wn = turtle.Screen()  # Creates a playground for turtles
wn.bgcolor("turquoise");


alex = turtle.Turtle()  # Create a turtle, assign to alex
alex.pencolor('yellow')
alex.pensize(1)
alex.speed(11)
alex.penup()

alex.setposition(200,200)


mysize = 300
alex.pendown()
drawHexagon(mysize, 90)
for i in range(mysize, 0, -4):
    draw2lines(i, 90)

turtle.done()
