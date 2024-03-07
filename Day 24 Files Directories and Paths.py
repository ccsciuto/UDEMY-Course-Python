with open("my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

with open("new_file.txt", mode="a") as file:
    content = file.write("New Text.")
    print(content)


