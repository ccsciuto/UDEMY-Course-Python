# running inputs inside functions

def greet():
    print("Hello welcome to the decoder.")
    print("This code will allow you to write a message in a code.")
    print("And it will let you decode ")

greet()

# function that allows for input
def greet_with_name(name):
    print(f"Hello {name} welcome to the decoder.")
    print("This code will allow you to write a message in a code.")
    print("And it will let you decode other code.")
# papameter = arguement
greet_with_name("Cecelia")

# functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}, welcome to the decoder.")
    print(f"How is the weather in {location}")

greet_with(location="Austin",name="Cecelia")

# calculating how many cans
import math

test_height = int(input("What is the height of the wall?\n"))
test_length = int(input("What is the length of the wall?\n"))
test_coverage = 5
paint_calc = (height=test_height, length=test_length, coverage=test_coverage)

def paint_calc(height, length, coverage):
    num_cans = (height*length)/coverage
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")
paint_calc()

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % 1 == 0:
            is_prime = False
    if is_prime:
        print("Your number is a prime number.")
    else:
        print("Your number is not a prime number.")
n = int(input("Choose a number.\n"))
prime_checker(number=n)

# decoding words

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plaintext, shift_amount):
    cipher_text = " "
    for letter in plaintext:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded word is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = " "
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded word is {plain_text}")

if direction == "encode":
    encrypt(plaintext=text,shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)
else:
    print("You didnt choose one of the options silly.")

# combining the function
def cesaer(starttext, shiftamount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shiftamount *= -1
    for char in starttext:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shiftamount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction} word is {end_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesaer(starttext=text,shiftamount=shift,cipher_direction=direction)
    results = input("Would you like to continue?\n")
    if results == "no":
        should_continue = False
        print("Goodbye")
