import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

sidenumber = 7
side_length = 80
angle = 360.0 / sidenumber
for i in range(sidenumber):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()