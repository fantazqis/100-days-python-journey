import turtle
import pandas
from marker import ProvinceMarker

marker = ProvinceMarker()
screen = turtle.Screen()
screen.setup(width=1050, height=788)
screen.title("Indonesia Provinces Game")
image = "blank_province.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = 0
# def mouse_clicked(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_clicked)
#
# turtle.mainloop()

while guessed_state < 50:
    user_answer = screen.textinput(title=f"{guessed_state}Guess the province", prompt="What is the province?").title()
    print(user_answer)
    # print(answer_province)

    data = pandas.read_csv("38_province.csv")
    # print(data.province)

    marker.check_answer(user_answer)
    guessed_state = guessed_state + 1



screen.exitonclick()
