import turtle

screen = turtle.Screen()
screen.bgcolor("orange")

my_turtle = turtle.Turtle()
my_turtle.color("black")
my_turtle.pensize(3)
my_turtle.speed(2)


for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

screen.exitonclick()
