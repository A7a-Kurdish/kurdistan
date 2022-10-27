import turtle
from turtle import*

screen = turtle.Screen()

t = turtle.Turtle()
speed(5000)

t.penup()
t.goto(-400, 250)
t.pendown()

t.color("red")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)

t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

t.penup()
t.goto(-57, -81)
t.pendown()
t.color("yellow")

t.penup()
t.goto(100, 0)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(2, 2)
t.pendown()
t.pensize(15)
for i in range(20):
	t.forward(150)
	t.backward(150)
	t.left(20)

turtle.done()
