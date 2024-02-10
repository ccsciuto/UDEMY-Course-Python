# converting data type

num_char = len(input("What is your name? "))
name_len = str(num_char)
print("Your name has " + name_len + " characters")

# calculating bmi
# bmi = weight(kg)/height**(m)
weight = int(input("what is your wieght in Kgs?  "))
height = float(input("what is your height in Meters? "))

bmi = round(weight/height **2, 2)
print(bmi)

# f strings
print(f"your bmi is {bmi}")

# weeks left to live

start_age = int(input("How old are you? "))
end_age = int(input("What age do you think you'll die at? "))
weeks_left = (end_age - start_age)*52
print(f"You have {weeks_left} weeks left")

# tip calculator

total_bill = float(input("What is yourr total bill? "))
tip_percent = float(input("What Percent would you like to tip? "))
people = float(input("How many people are splitting the bill? "))

amount = round((total_bill*(1+tip_percent/100))/people, 2)

print(f"Each person owes ${amount}")