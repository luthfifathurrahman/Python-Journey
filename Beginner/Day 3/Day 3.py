# if else statement
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster")
else:
    print("sorry you can't ride the rollercoaster")

# modulo operator (%)
number = int(input("what number you want to check? "))

if number % 2 == 0:
    print("it is even")
else:
    print("it is odd")

# Nested if else statement
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("how old are you? "))

    if age <= 18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("sorry you can't ride the rollercoaster")

# elif statement
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("how old are you? "))

    if age <= 12:
        print("pay $5")
    elif age <= 18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("sorry you can't ride the rollercoaster")

# multiple if statement
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("how old are you? "))

    if age <= 12:
        bill = 5
        print("child ticket are $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket are pay $7")
    else:
        bill = 12
        print("adult ticket are pay $12")

    photo = input("do you want photo? Y or N? ")
    if photo == "Y":
        bill += 3

    print(f"your bill is ${bill}")
else:
    print("sorry you can't ride the rollercoaster")

# PRACTICE: Pizza Order
print("welcome to the pizza deliveries")
size = input("what size do you want? S, M or L? ")
pepperoni = input("do you want to add a pepperoni? Y or N? ")
extra_cheese = input("do you want extra cheese? Y or N? ")
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")

# Logical Operators
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("how old are you? "))

    if age <= 12:
        bill += 5
        print("child ticket are $5")
    elif age <= 18:
        bill += 7
        print("Youth ticket are pay $7")
    elif age >= 45 and age <= 55:
        print("ticket price is $0")
    else:
        bill += 12
        print("adult ticket are pay $12")

    photo = input("do you want photo? Y or N? ")
    if photo == "Y":
        bill += 3

    print(f"your bill is ${bill}")
else:
    print("sorry you can't ride the rollercoaster")
