#!/usr/bin/python3
import turtle
import draw_shapes
#import 

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    draw_shapes.square(50)
    t.end_fill()

if __name__ == "__main__":
    t = turtle.Turtle()
    s = turtle.Screen()
    s.onscreenclick(drawit) ## apply mouse click events
    turtle.mainloop()
