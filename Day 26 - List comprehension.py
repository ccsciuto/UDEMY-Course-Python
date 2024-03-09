# # list comprehension
# list1 = [1, 2, 3, 4]
# list2 = [n + 1 for n in list1]
# print(list1)
# print(list2)
# name = "cecelia"
# letters = [letter for letter in name]
# print(letters)
# num = [n*2 for n in range(1, 5)]
# print(num)
# names = ["cecelia", "sydney", "alec", "josh", 'gus']
# short_names = [n for n in names if len(n) < 5]
# print(short_names)
# upper_names = [n.upper() for n in names]
# print(upper_names)
# num = [1, 1, 2, 4, 5, 7, 12, 14, 25]
# sq_num = [n**2 for n in num]
# print(sq_num)
# even_num = [n for n in sq_num if n%2 == 0]
# print(even_num)
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# results = [int(n) for n in list1 if n in list2]
# print(results)
# import random as r
# names = ["cecelia", "sydney", "alec", "josh", 'gus']
# scores = {student:r.randint(1, 100) for student in names}
# print(scores)
# passed_students = {key:value for (key, value) in scores.items() if value > 70}
# print(passed_students)
# sentence = input()
# list1 = sentence.split()
# print(list1)
# list2 = {word:len(word) for word in list1}
# print(list2)
# import pandas as pd
# weather = {
#     "Monday": 12,
#     "Tuesday": 25,
#     "Wednesday": 9,
#     "Thursday": 8,
#     "Friday": 14,
#     "Saturday": 21,
#     "Sunday": 11,
# }
# converted = {day:((temp*9/5)+32) for (day, temp) in weather.items()}
# print(converted)
# df = pd.DataFrame(weather, index=[0])
# print(df)
import pandas as pd

alpha = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in alpha.iterrows()}
print(dict)
name = input("Whats your Name?: ").upper()
words = [dict[l] for l in name]
print(words)
