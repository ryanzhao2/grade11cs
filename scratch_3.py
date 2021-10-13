import turtle
title = "Turtle Options"
print(title)
print("-"*len(title))

print("arrow, turtle, circle, square, triangle, classic")
user_shape = input("\nEnter the shape you would like to use ")
tula = turtle.Turtle()
tula.shape(user_shape)
tula.stamp()
turtle.done()