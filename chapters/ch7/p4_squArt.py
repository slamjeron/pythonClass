from turtle import Turtle
import random


def randomColor():
    r = random.randrange(0, 100)
    g = random.randrange(0, 100)
    b = random.randrange(0, 100)
    return (r / 100, g / 100, b / 100)


def drawRect(t, x, y, x2, y2):
    t.fillcolor(randomColor())
    t.begin_fill()
    t.setpos(x, y)
    t.down()
    t.pos()
    t.setpos(x, y2)
    t.pos()
    t.setpos(x2, y2)
    t.pos()
    t.setpos(x2, y)
    t.pos()
    t.setpos(x, y)
    t.pos()
    t.up()
    t.end_fill()


def recur(t, x, y, x2, y2, siz):
    drawRect(t, x, y, x2, y2)
    r = random.randrange(0, 2)
    if (siz > 0):
        if (r == 0):
            recur(t, x * (1 / 3), y, x2, y2, siz - 1)
            recur(t, x, y, x2 * (1 / 3), y2, siz - 1)
        else:
            recur(t, x, y, x2, y2 * (1 / 3), siz - 1)
            recur(t, x, y * (1 / 3), x2, y2, siz - 1)
level=int(input('enter a level: '))


td = Turtle()
td.up()
recur(td, -150, 100, 150, -100, level)
