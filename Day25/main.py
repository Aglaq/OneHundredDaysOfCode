# Day 25 - Working with CSV Data and the Pandas Library
# Day 25 - Project: Name the States
import turtle
import pandas
from write import Write

game_is_on = True
screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
states = states_data.state
guessed_states = []
points = 0
write = Write()

while game_is_on:
    answer_state = (screen.textinput(title=f"{points}/50 States Correct", prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        break

    for s in states:
        if answer_state == s:
            position = states_data[states_data.state == answer_state]
            position_x = position.x.item()
            position_y = position.y.item()
            write.update_screen(answer_state, position_x, position_y)
            guessed_states.append(answer_state)
            points += 1
        if points == 50:
            game_is_on = False

missing_states_list = []
for s in states:
    if s not in guessed_states:
        missing_states_list.append(s)

missing_states = pandas.DataFrame(missing_states_list)
missing_states.to_csv("states_to_learn.csv")

# Examples and exercises Day 25
# import pandas

# squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colors = squirrels_data["Primary Fur Color"]
# gray = colors.str.count("Gray")
# red = colors.str.count("Cinnamon")
# black = colors.str.count("Black")
# sum_of_gray = gray.sum(min_count = 1)
# sum_of_red = red.sum(min_count = 1)
# sum_of_black = black.sum(min_count = 1)

# final_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [sum_of_gray, sum_of_red, sum_of_black],
# }
# final_table = pandas.DataFrame(final_dict)
# final_table.to_csv("squirrel_count.csv")

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
