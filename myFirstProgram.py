import turtle

def drawHexagon(length, angle):
    alex.left(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)
    alex.right(angle)
    alex.forward(length)  # Tell alex to move forward by 50 units
    alex.right(angle)
    alex.forward(length)
    alex.right(120)
    alex.forward(15)
wn = turtle.Screen()  # Creates a playground for turtles
wn.bgcolor("turquoise");


alex = turtle.Turtle()  # Create a turtle, assign to alex
alex.pencolor('yellow')
alex.pensize(1)

for i in range(100, 9, -15):
      # Tell alex to move forward by 50 units
    drawHexagon(i,60)


               # Tell alex to turn by 90 degrees
    # Complete the second side of a rectangle
    # 36 degrees for a star
turtle.done()

