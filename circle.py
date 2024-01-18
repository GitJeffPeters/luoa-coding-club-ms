"""
File: circle.py
Project 7.1

Draws a circle.

1. The inputs are the coordinates of the center point and the radius.

"""
#thiis is a change.
import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)
    

def main():
    x = 50
    y = 75
    radius = 100
    drawCircle(Turtle(), x, y, radius)

if __name__ == "__main__":
    main()
