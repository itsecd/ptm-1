#!/usr/bin/env python
# Author - Anurag Rana

import turtle
from random import randint

BG_COLOR = "#0080ff"
colors = {
    "r": "red",
    "w": "white",
    "g": "green",
    "y": "yellow",
}

def create_rectangle(turtle: any, color: str, x: int, y: int,\
                     width: int, height: int) -> None:
    """creating a rectangle

    Args:
        turtle (any)
        color (str)
        x (int)
        y (int)
        width (int)
        height (int)
    """
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()   
    turtle.setheading(0)


def create_circle(turtle: any, x: int, y: int, radius: int, color: str) -> None:
    """creating a circle

    Args:
        turtle (any)
        x (int)
        y (int)
        radius (int)
        color (str)
    """
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()

oogway = turtle.Turtle()
oogway.speed(2)
screen = oogway.getscreen()
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")
screen.setup(width = 1.0, height = 1.0)

y = -100
x_rectangle = -15
y_rectangle = y-60
width_rectangle = 30
height_rectangle = 60
create_rectangle(oogway, colors["r"], x_rectangle, y_rectangle, \
                 width_rectangle, height_rectangle)

width = 240
oogway.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(oogway, colors["g"], x, y, width, height)
    y = y + height

oogway.speed(1)
oogway.penup()
oogway.color(colors[4])
oogway.goto(-20, y + 10)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
    oogway.forward(40)
    oogway.right(144)
oogway.end_fill()

tree_height = y + 40

x_circle = 230
y_circle = 180
radius_circle = 60
color_circle = colors["w"]
create_circle(oogway, x_circle, y_circle, radius_circle, color_circle)
x_circle= 220
create_circle(oogway, x_circle, y_circle, radius_circle, BG_COLOR)

oogway.speed(10)
number_of_stars = randint(20, 30)

for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width() // 2), screen.window_width() // 2)
    y_star = randint(tree_height, screen.window_height() // 2)
    size = randint(5, 20)
    oogway.penup()
    oogway.color(colors["w"])
    oogway.goto(x_star, y_star)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(size)
        oogway.right(144)
    oogway.end_fill()

oogway.speed(1)
oogway.penup()
msg = "Merry Christmas from ThePythonDjango.Com"
oogway.goto(0, -200)  
oogway.color(colors["w"])
oogway.pendown()
oogway.write(msg, move = False, align = "center", font = ("Arial", 15, "bold"))

oogway.hideturtle()
screen.mainloop()

