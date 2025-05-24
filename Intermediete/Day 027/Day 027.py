# Graphical User Interfaces
# with Tkinter and Function Arguments
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # padding

# Label
my_label = Label(text="I Am a Label",
                         font=("Arial", 24, "bold"))
# change the properties
# my_label["text"] = "New Text"
# my_label.config(text="new text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
def button_clicked():
    word = input.get()
    my_label.config(text=word)

button1 = Button(text="I'm a Button click me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="new button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry/Input
input = Entry(width=30)
input.insert(END, string="this is Entry box")
input.grid(column=4, row=3)

# Text Box
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=4, row=4)

# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=4, row=5)

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=4, row=6)

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=4, row=7)

# Radiobutton
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=4, row=8)
radiobutton2.grid(column=4, row=9)


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=4, row=10)

# let the window stay on
window.mainloop()