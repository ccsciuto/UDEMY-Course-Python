# # dictionaries
# programming_dictionary = {
#     "Bug": "An Error in a program that prevents it from running successfully",
#     "Function":"A piece of code that you can call over and over again",
#     "Loop":"The action of doing something over and over again"
# }
# print(programming_dictionary["Bug"])
#
# # adding entries to dict
# programming_dictionary["Def"] = "the word used to define a function"
# print(programming_dictionary)
#
# emp_dictionary = {}
#
# # wipe an existing dictionary
# # programming_dictionary = {}
#
# # edit an item in a dictionary
#
# programming_dictionary["Bug"] = "Changing the value of bug"
# print(programming_dictionary)
#
# # looping thru a dictionry
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
# grading student papers
# student_grades ={}
# student_scores = {
#     "Harry": 87,
#     "Sally": 45,
#     "Chad": 25,
#     "Josh": 98,
#     "Cecelia": 99
# }
# # assigning a grade with a loop
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 70:
#         student_grades[student] = "Average"
#     elif score > 50:
#         student_grades[student] = "Bad"
#     else:
#         student_grades[student] = "Failing"
#
# print(student_grades)
# # nest a list ina  dict
# capitols = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
# travel_log = {
#     "France":["Paris" ,"Lille","Dijon"],
#     "Germany":["Berlin","Munich"]
# }
# # nest a dict in a dict
# travel_count = {
#     "France":{"Cities_visited":["Paris","Lille","Dijon"],"Total_Visits": 12},
#     "Germany":{"Cities_visited":["Berlin","Munich"],"Total_Visits": 3}
# }
#
# # nests a dict ina list
#
# travel_log = [
#     {
#     "Country": "France",
#     "Cities_visited":["Paris","Lille","Dijon"],
#     "Total_Visits":  12
#     },
#     {
#     "Country": "Germany",
#     "Cities_visited":["Berlin","Munich"],
#     "Total_Visits": 3
#     }
# ]
#
#
# Country = input()
# Total_Visits = input()
# Cities_visited = input()
#
# def add_new_country(names, visited, cities):
#     new_country = {}
#     new_country["Country"] = names
#     new_country["Total_Visits"] = visited
#     new_country["Cities_visited"] = cities
#     travel_log.append(new_country)
# add_new_country(Country, Total_Visits, Cities_visited)
#
# print(f"Ive been to {travel_log[0]['Country']} {travel_log[0]['Total_Visits']} times.")
# print(f"My favorite city was {travel_log[0]['Cities_visited'][2]}.")
#
# creating a bid system

from replit import clear

bids = {}
bidding_finished = False
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_total = bidding_record[bidder]
        if bid_total > highest_bid:
            highest_bid = bid_total
            winner = bidder
    print(f"{winner} is the winner. They won with a bid amount of {bid_total}.")

while not bidding_finished:
    name = input("What is your name?\n")
    bid_amount = int(input("How much would you like to bid?\n"))
    bids[name] = bid_amount
    should_cont = input("Are there any other bidders?\n")
    if should_cont == "No":
        bidding_finished = True
    else:
        clear()
highest_bidder(bids)