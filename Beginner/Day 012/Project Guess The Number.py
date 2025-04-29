from xml.dom.minidom import ProcessingInstruction

from art import logo
import random

GUESS_NUMBER = random.randint(1, 100)

def ask_guess():
    """
    Ask the user to guess the number
    :return: number the user guessed int
    """
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Wrong input, please enter a valid number.")

def score(guess_number, answer, attempts):
    """
    Calculate the attempts left
    :param guess_number: Number the user need to guessed int
    :param answer: number the user guessed int
    :param attempts: attempts left int
    :return:
    """
    if answer == guess_number:
        print("You Won!")
        return True, attempts
    elif answer > guess_number:
        print("Too High!")
        attempts -= 1
    elif answer < guess_number:
        print("Too Low!")
        attempts -= 1

    if attempts == 0:
        print("You Lost!")
        return True, attempts
    else:
        return False, attempts

def guess_the_number():
    difficulty = input("Choose the difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
        print(GUESS_NUMBER)
        correct = False
        while not correct:
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = ask_guess()
            correct, attempts = score(GUESS_NUMBER, user_guess, attempts)
    elif difficulty == 'hard':
        attempts = 5
        print(GUESS_NUMBER)
        correct = False
        while not correct:
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = ask_guess()
            correct, attempts = score(GUESS_NUMBER, user_guess, attempts)
    else:
        print("Wrong input")
        guess_the_number()

print(logo)
print("Welcome to The Guess The Number Game!")
print("I'm thinking of number from 1 to 100.")
print("Your job is to guess it.")
print("First, you need to choose the difficulty level.")
guess_the_number()