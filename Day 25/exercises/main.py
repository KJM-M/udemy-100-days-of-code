# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)


# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# import pandas
# data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in Columns
# print(data["condition"])
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = monday["temp"]
# print((monday_temp * (9/5)) + 32)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Ami", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_d = pandas.DataFrame(data_dict)
# data_d.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260323.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./squirrels_data.csv")