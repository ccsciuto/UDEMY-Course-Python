from tkinter import *
import random
from tkinter import messagebox
import json


CHOICES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"/", "!", "@", "#", "?", "$", "<", ">", "*", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# functions
def save_submission():
    website = website_entry.get()
    email = email_entry.get()
    password_used = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password_used,
        }
    }
    if website == "" or password_used == "" or email == "":
        messagebox.showerror(title="Empty Field", message="Dont leave any fields empty!")
    else:
        try:
            with open("password_manager.json", "r") as file:
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
                data.update(new_data)
            with open("password_manager.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def password_generator():
    password = ""
    password_entry.delete(0, END)
    for _ in range(10):
        rand_choice = str(random.choice(CHOICES))
        password += rand_choice
    password_entry.insert(0, password)


def search_password():
    website = website_entry.get()
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Currently no passwords saved")
    else:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            if website in data:
                email = data[website]["Email"]
                password = data[website]["Password"]
                messagebox.showinfo(title=website, message=f"Username: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="No Website", message="No Website Found")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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
website_entry = Entry(width=21, bg="white", fg="black")
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=36, bg="white", fg="black")
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ceceliasciuto@gmail.com")
password_entry = Entry(width=21, bg="white", fg="black")
password_entry.grid(column=1, row=3)
# button
generate_pw = Button(text="Generate Password", bg="white", command=password_generator, fg="black")
generate_pw.grid(column=2, row=3)
add_button = Button(text="Add to File", width=36, command=save_submission)
add_button.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", bg="white", command=search_password, width=12)
search.grid(column=2, row=1)
window.mainloop()
