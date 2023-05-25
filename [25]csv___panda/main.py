# with open("./[25]csv_&_panda/weather_data.csv") as data:
#     info = data.readlines()
#     print(info)

# import csv

# with open("./[25]csv_&_panda/weather_data.csv") as data:
#     info = csv.DictReader(data)
#     temperatures = []
#     for row in data:
#         if row.split(",")[1] != "temp":
#             temperatures.append(int(row.split(",")[1]))

#     print(temperatures)

# import pandas

# data = pandas.read_csv("./[25]csv_&_panda/weather_data.csv")


# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"] <- how to get row
# farenheit = (monday.temp * 1.8) + 32
# print(farenheit)

#create a dataframe
# data_dict = {
#     "Name": ["Vanshav", "Keshav", "Ritu", "Arun", "Kanta"],
#     "Age": [15, 17, 41, 47, 71]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("./[25]csv_&_panda/family_info.csv")

import pandas
squirrel_data = pandas.read_csv("./[25]csv_&_panda/Squirrel_Data.csv")
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
final_data = pandas.DataFrame(data_dict)
final_data.to_csv("./[25]csv_&_panda/squirrel_fur_data.csv")