from tkinter import *

FONT = ("Courier", 10)

def button_clicked():
    """when the button clicked, convert miles to km"""
    miles = float(input.get())
    km = str(miles * 1.60934)
    label_KM.config(text=km)

window = Tk()
window.title("Mile To KM Converter") # window title
window.config(padx=20, pady=20) # window padding
window.bind('<Return>', lambda event:button_clicked())

# Entry
input = Entry(width=15, justify="center", font=FONT)
input.focus()
input.insert(END, string="0")
input.grid(column=1, row=0)

# Label Miles
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row =0)

# Label Equal
label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row =1)

# Label KM
label_KM = Label(text="0", font=FONT)
label_KM.grid(column=1, row =1)

# Label KM Text
label_KM_text = Label(text="KM", font=FONT)
label_KM_text.grid(column=2, row =1)

# Button Calculate
button_calculate = Button(text="Calculate", font=FONT, width=15, command=button_clicked)
button_calculate.grid(column=1, row=2)

window.mainloop()