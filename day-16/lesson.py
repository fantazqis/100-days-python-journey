import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Flower")

t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Colors for the flower
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

# Draw spiral flower
for i in range(1000):
    t.color(colors[i % len(colors)])
    t.width(2)
    t.forward(i * 0.5)
    t.left(59)

# Draw center circle
t.penup()
t.goto(0, -20)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(20)
t.end_fill()

# Keep window open
turtle.done()