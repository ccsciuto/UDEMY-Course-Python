# import csv
# import pandas
#
# # with open ("weather_data.csv") as data:
# #     data_file = csv.reader(data)
# #     temps = []
# #     for row in data_file:
# #         if row[1] != "temp":
# #             temps.append(int(row[1]))
# #     print(temps)
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].tolist()
# avg_temp = sum(temp_list)/len(temp_list)
# print(data["temp"].max())
# print(data["temp"].mean())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print((data[data.day == "Monday"].temp * 9/5)+32)
#
# # create a df from scratch
#
# data_dictionary = {
#     "students": ["amy", "chad", "tyler"],
#     "scores": [95, 76, 87]
#
# }
#
# df = pandas.DataFrame(data_dictionary)
# print(df)
#
# import pandas as pd
#
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# df = pd.DataFrame(data)
# grouped_data = df.groupby(["Primary Fur Color"]).count().reset_index()
# grouped_data["Count"] = grouped_data["X"]
# new_df = grouped_data[["Primary Fur Color", "Count"]]
# new_df.to_csv("sqrl_count", index=False)
# us states quiz
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct.",
                                    prompt="Whats another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




