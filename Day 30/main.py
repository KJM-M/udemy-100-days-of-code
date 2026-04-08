from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    new_data = {
        website: {
        "email": email,
        "password": password,
        }
    }

    if website and email and password:
        try:
            with open("saved_data.json", "r") as file:
                #Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("saved_data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("saved_data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")

# ----------------------------- SEARCH -------------------------------- #

def find_password():
    try:
        with open("saved_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")

    else:
        website = website_entry.get().strip()
        site_data = data.get(website)
        if site_data:
            email = site_data["email"]
            password = site_data["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(120, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(window, text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1, sticky="EW")
email_entry = Entry(width=35)
email_entry.insert(0, "test@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
search_btn = Button(text="Search", width= 15, command=find_password)
search_btn.grid(column=2, row=1)


window.mainloop()
