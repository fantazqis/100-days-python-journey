from turtle import Turtle, Screen
import random
#
# def jalan(num):
#     if num == 1:
#         timmy.right(90)
#         timmy.forward(50)
#     elif num == 2:
#         timmy.left(90)
#         timmy.forward(50)
#     elif num == 3:
#         timmy.back(50)
#         timmy.forward(50)
#     elif num == 4:
#         timmy.forward(50)
#
def warna_rgb():
    warna_r = random.randint(1,255)
    warna_g = random.randint(1,255)
    warna_b = random.randint(1,255)

    return warna_r, warna_g, warna_b


def spinograph():
    timmy.circle(100)
    timmy.right(10)


screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(10)
i = 2




# timmy.pensize(5)
# i =7
#
# while i < 10:
#     cc=random.randint(1, 4)
#     jalan(cc)
#     warna = warna_rgb()
#     timmy.color(warna)

while i < 10:
    spinograph()
    warna = warna_rgb()
    timmy.color(warna)



screen.exitonclick()