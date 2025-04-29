# Function with output
def my_function():
    return 3 * 2

output = my_function()
print(output)

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("luthfi", "fathurrahman")
print(formated_string)

def func_1(text):
    return text + text

# use output from function as an input in another function
def func_2(text):
    return text.title()

output_1 = func_2(func_1("hello"))
print(output_1)

# multiple return values
def format_name_new(f_name, l_name):
    """
    this one called doc string.
    take a first and last name
    and format it to return
    the title case version
    """
    if f_name == "" or l_name == "":
        return "the input is not complete"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name_new(input("what is your first name? "), input("what is your last name? ")))

# exercise
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
    else:
        return "No Leap"

print(is_leap_year(2000))

