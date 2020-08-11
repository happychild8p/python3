#!/usr/bin/python3
import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

def polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)


t.up()
t.goto(-200,0)
t.down()
square(100)
t.up()
t.goto(0,0)
t.down()
triangle(100)
t.up()
t.goto(200,0)
t.down()
polygon(5,100)
t.up()
t.goto(400,0)
t.down()
polygon(6,50)
