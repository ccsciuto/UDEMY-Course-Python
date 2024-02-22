# creating a blackjack game

# deal/choose 2 cards for the player and the dealer
# reveal which cards were dealt to the player and one card for the dealer
# let the player select whether they would like to choose another card
# let the dealter select if they want another card(is total is < 16)
# continue this loop if player selected another card
# once player does not want to sleect cards then show hands and determine winner

import random

def deal_cards():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calc_score(cards):
    """takes a list of cards and returns a score of those cards"""
    if sum(cards) and len(cards) == 2:
        return 0
    if 11 in cards and sum > 21:
        cards.remove(11)
        cards.append(1)
    sum(cards)
def compare_scores(player, dealer):
    if player_total == dealer_total:
        print("Draw")
    elif dealer_total == 0:
        print("Computer has blackjack")
    elif player_total == 0:
        print("You have blackjack!")
    elif player_total > 21:
        print("You went over. You lose")
    elif dealer_total > 21:
        print("Dealer went over. They lose")
    elif player_total > dealer_total:
        print("You Win!")
    else:
        print("Dealer Wins")

players_cards = []
dealers_cards = []
is_game_over = False
for _ in range(2):
    players_cards.append(deal_cards())
    dealers_cards.append(deal_cards())
while not is_game_over:
    player_total = calc_score(players_cards)
    dealer_total = calc_score(dealers_cards)
    print(f"Your cards are {players_cards} and the dealers first card is {dealers_cards[0]}")
    if player_total == 0 or dealer_total == 0 or player_total > 21:
        is_game_over = True
    else:
        select_another = input("would you like to select another card?(y or n)\n")
        if select_another == "y":
            players_cards.append(deal_cards())
        else:
            is_game_over = True
while dealer_total != 0 and dealer_total < 17:
    dealers_cards.append(deal_cards())
    dealer_total = calc_score(dealers_cards)

print(compare_scores(player_total,dealer_total))
# print(f"Your cards are {players_cards} Your current total is {player_total}")
# print(f"The dealers first card is {dealers_cards[0]}")
# continue_game = True
# if player_total == 21:
#     continue_game = False
# while continue_game:
#     select_another = input("would you like to select another card?(y or n)\n")
#     if select_another == "n":
#         while dealer_total < 17:
#             next_card = random.choice(cards)
#             dealers_cards.append(next_card)
#             dealer_total += next_card
#         continue_game = False
#         print("The game is over.")
#         if dealer_total > player_total and dealer_total < 22:
#             print(f"The dealer won with a score of {dealer_total}.")
#         elif dealer_total == player_total:
#             print("Its a draw!")
#         else:
#             print("You win!!")
#             print(dealer_total)
#             print(dealers_cards)
#     else:
#         next_card = random.choice(cards)
#         players_cards.append(next_card)
#         player_total += next_card
#         if player_total < 22:
#             print(f"Your current cards are {players_cards}")
#             print(f"Your new total is {player_total}")
#         else:
#             continue_game = False
#             print(f"You new score is {player_total} and you lost the game")
