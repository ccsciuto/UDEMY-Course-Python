# creating a password generator

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
students_height = input("What are the students heights?\n").split()

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
total_height = 0
for height in students_height:
    total_height += height
total_students = 0
for student in students_height:
    total_students += 1

print(f"total height is {total_height}")
print(f"total students is {total_students}")
average = round(total_height/total_students, 2)
print(f"The average height is {average}")
print(students_height)

student_scores = input("What are the students scores?\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score>highest_score:
        highest_score = score

print(f"The higest score in the class is {highest_score}")

# creating ranges in loops
total = 0
for number in range(1,101):
    total += number
print(total)

target = int(input("Give me a number bewteen 0 and 100\n"))
even_sum = 0
for number in range(2,target+1 ,2):
    even_sum += number
print(even_sum)

# fizzbuzz game

for n in range(1,101):
    if n%5 == 0 and n%3 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)

# py password genertor
import random
from random import shuffle
letters = ["a","b","c","d","e","f","g"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$"]

print("Welcome to the pypassword generator!!")
nm_letters = int(input("How many letters would you like in your password?\n"))
nm_numbers = int(input("How many numbers would you like in your password?\n"))
nm_symbols = int(input("How many symbols would you like in your password?\n"))
password = ""

for letter in range(0, nm_letters):
    password += random.choice(letters)
for number in range(0, nm_numbers):
    password += random.choice(numbers)
for symbol in range(0, nm_symbols):
    password += random.choice(symbols)

print(password)