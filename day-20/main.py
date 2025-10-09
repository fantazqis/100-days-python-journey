from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


strarting_position = [(0,0), (-20,0), (-40,0)]

segments = []

for position in strarting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

is_game_on = True
while is_game_on:
    segments[0].forward(10)
    segments[1].forward(10)
    segments[2].forward(10)
