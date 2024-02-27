Class is the blueprint of an object class has first letter capitalized
things that make up an object:
Attributes - what it holds(variables/lists etc
Methods - what the object does(functions)

from turtle import Turtle, Screen
toddy = Turtle()
print(toddy)
toddy.shape("turtle")
toddy.color("DeepPink")
toddy.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Distance", ["5K", "10K", "Half Marathon", "Marathon"])
table.add_column("PR", ["23:00", "49:44", "1:46:51", "3:59:17"])
table.add_row(["1 Mile", "7:21"])
print(table)
