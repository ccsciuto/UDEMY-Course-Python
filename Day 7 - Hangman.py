# creating a hangman game
from replit import clear
import random

word_list = ["slice", "pizza", "mathmatics", "applepie"]

chosen_word = random.choice(word_list)

# creating a list for blanks for the word
word = len(chosen_word)
blanks_list = []
for n in range(word):
    blanks_list += ["_"]
blank = "_"
guesses_left = word
end_of_game = False
print(guesses_left)
while not end_of_game:
    user_guess = input("What letter would you like to guess? \n").lower()
    if user_guess in blanks_list:
        print("You've already guessed this letter")
    for position in range(word):
        letter = chosen_word[position]
        if letter == user_guess:
            blanks_list[position] = user_guess
    print(f"{' '.join(blanks_list)}")
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        guesses_left -= 1
    clear()
    if  blank not in blanks_list or guesses_left == 0:
        end_of_game = True

if blank in blanks_list:
    print("You Lost")
else:
    print("You won")
# print(f"Congrats you won! the word was {chosen_word}.")
