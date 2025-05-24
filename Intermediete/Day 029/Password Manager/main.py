from tkinter import *
import random
from tkinter import messagebox
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    random_letters = random.sample(LETTERS, random.randint(8, 10))
    random_symbols = random.sample(NUMBERS, random.randint(2, 4))
    random_numbers = random.sample(SYMBOLS, random.randint(2, 4))

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)

    hard_pass = "".join([char for char in password_list])
    password_entry.insert(END, string=hard_pass)
    pyperclip.copy(hard_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    uname = email_uname_entry.get()
    password = password_entry.get()

    if (len(website) == 0) or (len(uname) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered:\n"
                                                 f"Email		: {uname}\n"
                                                 f"Password	: {password}\n"
                                                 f"Is it ok to save?")

        if is_okay:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website} | {uname} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# WEBSITE LABEL
website_label = Label(text="Website		:")
website_label.grid(column=0, row=1)

# EMAIL/USERNAME LABEL
email_uname_label = Label(text="Email/Username	:")
email_uname_label.grid(column=0, row=2)

# PASSWORD LABEL
password_label = Label(text="Password	:")
password_label.grid(column=0, row=3)

# WEBSITE ENTRY
website_entry = Entry(width= 50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# EMAIL/USERNAME ENTRY
email_uname_entry = Entry(width= 50)
email_uname_entry.insert(END, string="luthfi@email.com")
email_uname_entry.grid(column=1, row=2, columnspan=2)

# PASSWORD ENTRY
password_entry = Entry(width= 32)
password_entry.grid(column=1, row=3)

# GENERATE PASSWORD BUTTON
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3)

# ADD BUTTON
add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()