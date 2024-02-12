import random
# producing random numbers

random_int = random.randint(0,200)
print(random_int)

# heads or tails
your_num = int(input("Pick a number between 1 and 100.\n"))

if your_num%2 ==0:
    print("Your number is even")
else:
    print("Your number is odd")

states = ["NH", "VT", "TX", "NY", "FL"]
states.append("CO")
print(states)

names = ["cece", "syd", "maddie"]
num = len(names)-1
selection = random.randint(0, num)
person_to_pay = names[selection]
print(f"Sorry {person_to_pay} has to pay the bill today")

# nested list
fruits = ["strawberries", "apples", "grapes", "watermelon"]
veggies = ["potato", "corn", "brocoli", "beans"]
dirty_food = [fruits, veggies]

print(dirty_food)

list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

map = [list1, list2, list3]
print("Hiding your treasue. X marks the spot!")
position = input()
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
num_index = int(position[1])-1
map[num_index][letter_index] = "x"
print(f"{list1}\n{list2}\n{list3}" )

# rock paper scissors

answer = ["rock", "paper", "scissor"]
your_guess = int(input("Choose rock(1), paper(2) or scissors(3).\n"))-1
computers_guess = random.randint(0, len(answer)-1)
if your_guess == computers_guess:
    print("its a draw!")
elif your_guess == 0 and computers_guess == 1:
    print(f"Computer guessed {answer[computers_guess]}! You Lose!")
elif your_guess == 1 and computers_guess == 0:
    print(f"Computer guessed {answer[computers_guess]}! You win!")
elif your_guess == 2 and computers_guess == 0:
    print(f"Computer guessed {answer[computers_guess]}! You Lose!")
elif your_guess == 0 and computers_guess == 2:
    print(f"Computer guessed {answer[computers_guess]}! You Win!")
elif your_guess == 1 and computers_guess == 2:
    print(f"Computer guessed {answer[computers_guess]}! You Lose!")
elif your_guess == 2 and computers_guess == 0:
    print(f"Computer guessed {answer[computers_guess]}! You Lose!")
else:
    print("you choose an invalid number. you lose")

