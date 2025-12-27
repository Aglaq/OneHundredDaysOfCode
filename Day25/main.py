# Day 25 - Working with CSV Data and the Pandas Library
# Day 25 - Project: Name the States
import pandas






# Examples and exercises Day 25
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temperature_c = monday.temp
# temperature_f = (temperature_c * 9 / 5) + 32
# print(temperature_f)

# Create dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures_column = []
#     temperatures = []

#     for row in data:
#         temp = row[1]
#         temperatures_column.append(temp)

#     for value in temperatures_column[1:]:
#         temp_int = int(value)
#         temperatures.append(temp_int)

# print(temperatures)

# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)
