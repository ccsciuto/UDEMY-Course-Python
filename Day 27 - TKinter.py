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

window = Tk()
window.title("First Program")
window.minsize(width=500, height=300)