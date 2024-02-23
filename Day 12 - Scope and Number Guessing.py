# understanding scope
# local scope
enemies = 1

def adding_enemy():
    # enemy only has local scope since its inside the function
    enemies = 2
    print(f"enemies inside function: {enemies}")

adding_enemy()
print(f"enemies outside the function: {enemies}")

# global scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(potion_strength)
# whenever you give name to anything you need tobe aware of where you create them

# no such thing as block scope
if 3 > 2:
    new_variable = 0
game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]
# can still assign variables with if/while/for statement
print(new_enemy)

# modifying global scope
enemies = 1

def adding_enemy():
    # enemy only has local scope since its inside the function
    # this actually creates a new variable. it doesnt actually change the variable
    # try to not name your local and global varibales the same name
    print(f"enemies inside function: {enemies}")
    return enemies + 1

adding_enemy()
print(f"enemies outside the function: {enemies}")

# changing variables vs constants
# most variables that shouldnt be modified should be in all caps

# number guessing game
import random
EASY_LEVEL = 10
HARD_LEVEL = 5
def check_answer(guess, answer, turns):
    """checks answer against geuss and returns number against guess"""
    if guess == answer:
        print("Nice! You picked the right number!")
    elif guess < answer:
        print("You're too low. Guess again!")
        return turns - 1
    else:
        print("You're too high. Guess again!")
        return turns - 1
def set_difficulty():
    selected_level = input("Would you like to play on 'easy' or 'hard' mode?\n")
    if selected_level == "easy":
         return EASY_LEVEL
    elif selected_level == "hard":
         return HARD_LEVEL
    else:
        print("You didnt choose a correct level.")
def game():
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    computers_number = random.randint(1, 100)
    print(computers_number)
    turns = set_difficulty()
    guess = 0
    while guess != computers_number:
        print(f"You have {turns} turns remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,computers_number,turns)
        if turns == 0:
            print("You've run out of guesses. You Lose")
            return
game()

# my attempt
def number_guess(level):
    guesses_remaining = guesses
    print(f"You have {level} guesses remaining.")
    players_guess = int(input("What number would you like to guess?\n"))
    if players_guess == computers_number:
        correct_number = True
        print("Nice! You picked the right number!")
    elif players_guess < computers_number and guesses_remaining > 0:
        print("You're too low. Guess again!")
        guesses_remaining = guesses_remaining - 1
    elif players_guess > computers_number and guesses_remaining > 0:
        print("You're too high. Guess again!")
        guesses_remaining = guesses_remaining - 1
    else:
        print("Sorry you ran out of guesses!")

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
selected_level = input("Would you like to play on 'easy' or 'hard' mode?\n")
if selected_level == "easy":
    guesses = 10
elif selected_level == "hard":
    guesses = 5
else:
    print("You didnt choose a correct level.")
computers_number = random.randint(1, 100)
print(computers_number)
correct_number = False
while not correct_number:
    number_guess(guesses)

