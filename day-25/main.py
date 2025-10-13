import csv
import pandas
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
# temp_total = 0
data = pandas.read_csv("weather_data.csv")
# list_data = data["temp"].to_list()
# for temp in list_data:
#     temp_total += float(temp)

# average_temp = temp_total / len(list_data)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp = monday.temp[0]

print(temp)

data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")