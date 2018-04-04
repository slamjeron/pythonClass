from turtle import Turtle
import random


def randomColor():
    r = random.randrange(0, 100)
    g = random.randrange(0, 100)
    b = random.randrange(0, 100)
    return (r / 100, g / 100, b / 100)


def drawRect(t, width, hight):
    t.up()
    t.down()
    t.forward(hight)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(hight)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.up


def draw_koch_segment(t, run, mydepth, depth):
    if mydepth == depth:
        # Just draw a segment
        t.begin_fill()
        drawRect(t, run, run * 2 / 3)
        t.end_fill()
    else:
        myrun = run * 2 / 3
        # Make each straight bit into a smaller version of ourselves
        t.down()
        t.begin_fill()
        drawRect(t, run, myrun)

        t.end_fill()
        t.pencolor(randomColor())
        t.fillcolor(randomColor())
        draw_koch_segment(t, myrun, mydepth + 1, depth)


td = Turtle()
td.penup()
td.setposition(-370, 300)
td.pendown()
td.left(270)
td.pencolor(randomColor())
td.fillcolor(randomColor())

draw_koch_segment(td, 500, 0, 1)
