#!/usr/bin/python3
import turtle

def turn_left():
    t.left(10)
    t.forward(10)
def turn_right():
    t.right(10)
    t.forward(10)
def move_forward():
    t.forward(10)
def move_back():
    t.back(10)

if __name__ == "__main__":
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(move_forward, "Up")
    screen.onkey(move_back, "Down")
    screen.listen()

    turtle.mainloop()
