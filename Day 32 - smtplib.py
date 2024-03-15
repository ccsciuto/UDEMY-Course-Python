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
import datetime as dt

today = dt.datetime.now()
print(today)
