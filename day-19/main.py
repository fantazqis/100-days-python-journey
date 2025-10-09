from turtle import Turtle, Screen
import random

def init(dict, list):
    turtle_name = "tim"
    for i in range(5):
        name = turtle_name + str(i)
        turtles[name] = Turtle()
        turtles[name].shape("turtle")
        turtles[name].color(list[i])
        turtles[name].penup()
        turtles[name].goto(-400, i * 50)

screen = Screen()
screen.setup(width=850, height=600)
turtles = {}
color = ["red", "blue", "green", "black", "purple"]
init(dict = turtles, list = color)

user_bet = screen.textinput(title="Taruhan taruhan", prompt=f"warna apa yang bakal menang? {color}").lower()

is_race_on = True
while is_race_on:
    for turtle_name in turtles:
        turtles[turtle_name].forward(random.randint(1,10))
        if turtles[turtle_name].xcor() > 410:
            is_race_on = False
            winning_color = turtles[turtle_name].pencolor()
            message_turtle = Turtle()
            message_turtle.hideturtle()
            message_turtle.penup()
            message_turtle.goto(0, 0)
            if winning_color == user_bet:
                message_turtle.write("SELAMAT, ANDA MENANG! 🎉", align="center", font=("Arial", 24, "bold"))
            else:
                message_turtle.write(f"ANDA KALAH! Pemenang: {winning_color}", align="center",
                                     font=("Arial", 24, "bold"))

screen.exitonclick()