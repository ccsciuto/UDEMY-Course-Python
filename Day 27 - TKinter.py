# from tkinter import *
#
#
# window = Tk()
# window.title("First Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=200)
#
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text=input.get())
#
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=2,row=3)
# my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.grid(column=6,row=3)
# input = Entry(width=10)
# input.grid(column=2,row=0)
# input.get()
# window.mainloop()
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# print(add(1,2,3,4,5,6,7,8,9,10))
#
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = Tk()
window.title("First Program")
window.config(padx=20, pady=20)
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal = Label(text="is equal to")
is_equal.grid(column=0,row=1)
km_result = Label(text="0")
km_result.grid(column=1,row=1)
km_label = Label(text="Km")
km_label.grid(column=2,row=1)
calc = Button(text="Convert", command=miles_to_km)
calc.grid(column=1, row=2)
window.mainloop()