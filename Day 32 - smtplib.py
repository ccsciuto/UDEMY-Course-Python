# import smtplib
#
# my_email = "ceceliasciuto@gmail.com"
# password = "txmssbqqxmcfdems"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ceceliasciuto@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")
# import datetime as dt
# import random
# import smtplib
#
#
# EMAIL = "ceceliasciuto@gmail.com"
# PASSWORD = "txmssbqqxmcfdems"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 5:
#     with open("quotes.txt") as quote:
#         all_quotes = quote.readlines()
#         random_quote = random.choice(all_quotes)
#     print(random_quote)
#     with smtplib.SMTP("smtp.gmail.com", 578) as connection:
#         connection.starttls()
#         connection.login(EMAIL, PASSWORD)
#         connection.sendmail(from_addr=EMAIL,
#                             to_addrs=EMAIL,
#                             msg=f"Subject:Monday Motivation\n\n{quote}")
##################### Normal Starting Project ######################
from datetime import datetime
import smtplib
import pandas as pd
import random

EMAIL = "ceceliasciuto@gmail.com"
PASSWORD = "txmssbqqxmcfdems"

today = (datetime.now().month, datetime.now().day)
file = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in file.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(EMAIL, PASSWORD)
    #     connection.sendmail(from_addr=EMAIL,
    #                         to_addrs=birthday_person["email"],
    #                         msg=f"Subject:Happy Birthday!\n\n{contents}")
print(contents)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


