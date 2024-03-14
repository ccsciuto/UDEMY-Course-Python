# # open file
# try:
#     file = open("a_file.txt")
#     name = "Cecelia"
#     add = name + " is perfect"
# except FileExistsError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except TypeError as error_message:
#     print(f"you cant add str and int: {error_message}")
# else:
#     print(f"successful! {add}")
# finally:
#     raise
# weight = float(input("What is your weight? "))
# height = float(input("What is your height? "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
# bmi = weight/height ** 2
# fruits = ['apple', 'peach', 'pumpkin']
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(int(input("pick a number pie: ")))
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
total_likes = 0
for posts in facebook_posts:
    try:
        total_likes = total_likes + posts["Likes"]
    except KeyError:
        posts[total_likes] = 0

print(total_likes)



