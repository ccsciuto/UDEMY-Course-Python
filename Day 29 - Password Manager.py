from tkinter import *
import random

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SIGN = ["/", "!", "@", "#", "?", "$", "<", ">", "*"]

# functions
def save_submission():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


def password_generator():
    password = ""
    # password_entry.delete(0, END)
    for _ in range(3):
        rand_num = str(random.randint(0, 9))
        rand_letter = random.choice(ALPHABET)
        rand_sign = random.choice(SIGN)
        password += rand_sign
        password += rand_letter
        password += rand_num
    password_entry.insert(0, password)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
canvas.config(bg="white")
# labels
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white", fg="black")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)
# entried
website_entry = Entry(width=35, bg="white", fg="black")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35, bg="white", fg="black")
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ceceliasciuto@gmail.com")
password_entry = Entry(width=21, bg="white", fg="black")
password_entry.grid(column=1, row=3)
# button
generate_pw = Button(text="Generate Password", bg="white", command=password_generator, fg="black")
generate_pw.grid(column=2, row=3)
add_button = Button(text="Add to File", width=36)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()