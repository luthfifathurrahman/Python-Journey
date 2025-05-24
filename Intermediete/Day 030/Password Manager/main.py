from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

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
def write_file(data_input):
    with open(file="data.json", mode="w") as file:
        json.dump(data_input, file, indent=4)

def save_password():
    website = website_entry.get()
    uname = email_uname_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": uname,
            "password": password,
        }
    }

    if (len(website) == 0) or (len(uname) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            is_okay = messagebox.askokcancel(title=website,
                                             message=f"These are the details entered:\n\n"
                                                     f"Email		: {uname}\n"
                                                     f"Password	: {password}\n\n"
                                                     f"Is it ok to save?")

            if is_okay:
                write_file(new_data)
        else:
            is_okay = messagebox.askokcancel(title=website,
                                             message=f"These are the details entered:\n\n"
                                                     f"Email		: {uname}\n"
                                                     f"Password	: {password}\n\n"
                                                     f"Is it ok to save?")

            if is_okay:
                # updating old data with new data
                data.update(new_data)
                write_file(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found",
                               message="No Data File Found")
    else:
        website = website_entry.get()
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title="Information", message=f"Here is your info:\n\nWebsite		: {website}\nEmail		: {email}\nPassword	: {password}\n\nThe password has been automatically copied to your clipboard.")
            pyperclip.copy(password)
        else:
            print(website)
            messagebox.showwarning(title="Not Found", message=f"No details for '{website}' found.")
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
website_entry = Entry(width= 32)
website_entry.focus()
website_entry.grid(column=1, row=1)

# EMAIL/USERNAME ENTRY
email_uname_entry = Entry(width= 50)
email_uname_entry.insert(END, string="luthfi@email.com")
email_uname_entry.grid(column=1, row=2, columnspan=2)

# PASSWORD ENTRY
password_entry = Entry(width= 32)
password_entry.grid(column=1, row=3)

# SEARCH BUTTON
generate_pass_button = Button(text="Search", width=14, command=find_password)
generate_pass_button.grid(column=2, row=1)

# GENERATE PASSWORD BUTTON
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3)

# ADD BUTTON
add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()