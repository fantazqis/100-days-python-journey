from turtle import Turtle
import pandas

class ProvinceMarker(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("38_province.csv")
        self.hideturtle()
        self.penup()

    def marker_position(self, province, x_coord, y_coord):
        self.goto(x_coord, y_coord)
        self.write(province)

    def check_answer(self, user_answer):
        for province in self.data.province:
            if province == user_answer:
                self.coordinate(user_answer)

    def coordinate(self, user_answer):
        coordinate = self.data[self.data.province == user_answer]
        x_coord = coordinate.x.iloc[0]
        y_coord = coordinate.y.iloc[0]

        self.marker_position(province=user_answer, x_coord=x_coord, y_coord=y_coord)