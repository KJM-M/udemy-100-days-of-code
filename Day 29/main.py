from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

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

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: \n{email} "
                                                              f"\n\nPassword: \n{password} \n\nIs it ok to save?")
        if is_ok:
            with open("saved_data.txt", "a") as file:
                file.write(f"{website.capitalize()} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


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


website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_entry = Entry(width=35)
email_entry.insert(0, "test@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
