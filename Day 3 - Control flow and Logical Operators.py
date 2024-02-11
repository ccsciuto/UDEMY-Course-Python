# using if statements
print("Welcome to the rollercoaster test")
height = int(input("What is your height? \n"))

if height>=120:
    print("You can ride!")
else:
    print("sorry youre too short")

# checking for odd numbers

number = int(input("give me a number "))

if number%2 == 0:
    print("Its even!")
else:
    print("Its odd!")

# nested if statements

age = int(input("What is your age? "))
height = int(input("what is your height? "))
bill = 0
if age <=18:
    if height < 100:
        print("You cant ride")
        bill += 0
    elif height < 120:
        print("you might be able to ride")
    else:
        print("you can ride")
        bill += 5
else:
    print("you can ride")
print(f"your bill is {bill}")
# calculating bmi
# bmi = weight(kg)/height**(m)
weight = int(input("what is your wieght in Kgs?  "))
height = float(input("what is your height in Meters? "))

bmi = round(weight/height **2, 2)

# f strings
print(f"your bmi is {bmi}")

if bmi > 10:
    print("youre pretty healthy")
else:
    print("Goodluck to you")

# ordering pizza and calc bill

pizza_size = input("What size pizza would you like (S, M L)? ")
pepperoni = input("Would you like pepperoni? ")
extra_cheese = input("Would you like extra cheese? ")
bill = 0
if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    bill += 5
else:
    bill

if extra_cheese == "Y":
    bill += 5
else:
    bill

print(f"Youre bill is ${bill}")

# love calculator
name_one = input("what is your name? ")
name_two = input("what is your lovers name? ")

combined_names = name_one + name_two
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

first_digit = t + r + u + e
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10:
    print("Breakup immidiately")
elif score < 50:
    print("You might stand a chance")
else:
    print("Lovers for life!!!!")

# ascii art

