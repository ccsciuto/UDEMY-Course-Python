# building a calculator app

def format_name(f_name,l_name):
    formated_first = f_name.title()
    formated_last = l_name.title()
    return f"{formated_first} {formated_last}"

first = input("What is your first name?\n")
last = input("What is your last name?\n")

formatted = format_name(first,last)
print(formatted)
# multiple return sytataments

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs"
    formated_first = f_name.title()
    formated_last = l_name.title()
    return f"{formated_first} {formated_last}"

formatted = format_name(input("What is your first name?\n"),input("What is your last name?\n"))
print(formatted)

#  calculating days in month
leap_year = False
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
              return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)

docstrings
def using_docstring():
    """This is how we add documentation to a function"""

# using_docstring()
# building a calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What is the first number?\n"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the list above:\n")
num2 = int(input("What is the second number?\n"))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")
operation_symbol = input("Pick another operation from the list:\n")
num3 = int(input("What is the third number?\n"))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

continue_calc = True
num1 = 0
while continue_calc:
    if num1 == 0:
        num1 = float(input("Choose a number?\n"))
    else:
        num1 = last_answer
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the list above:\n")
    num2 = float(input("What is the second number?\n"))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    last_answer = first_answer
    cont_calc = input(f"What you like to continue this calculation with {last_answer} or start a new calculation?(y for prev answer or n new answer or end to end the calc)")
    if cont_calc == "end":
        continue_calc = False
    elif cont_calc == "n":
        num1 = 0




