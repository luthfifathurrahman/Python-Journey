# debugging
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("you got it")
# my_function()
# The problem with the code above is the range(1, 20) it will never reach 20.
# we need to change the range to range(1,21)

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("you got it")

my_function()

# reproduce the bug
# from random import randint
# dice = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)
# print(dice[dice_num])
# the problem with the code above is in dice[dice_num]
# we need to change dice_num to dice_num - 1
from random import randint
dice = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6)
print(dice[dice_num - 1])

# another exercise
# year = int(input("what's your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# the problem with the code above is in year > 1994
# if the input is 1994, it will print nothing.
year = int(input("what's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

