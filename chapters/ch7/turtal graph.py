from turtle import Turtle

t = Turtle()
t.left(90)
t.forward(30)
t.left(90)
t.up()
t.forward(10)
t.setheading(0)
t.down()
t.forward(20)
t.hideturtle()
t.up()
t.goto(10, 10)
t.setheading(270)
t.down()
for count in range(4):
    t.forward(200)
    t.left(90)
