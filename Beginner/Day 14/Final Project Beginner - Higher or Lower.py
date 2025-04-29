import art
from game_data import data
import random

def randomize_number():
    return random.randint(0, len(data) - 1)

def randomize_next_number(list):
    while True:
        number_B = randomize_number()
        if number_B not in list:
            return number_B

def compare(A, vs, B):
    return f"Compare A: {data[A]["name"]}, a {data[A]["description"]} from {data[A]["country"]}\n{vs}\nAgainst B: {data[B]["name"]}, a {data[B]["description"]} from {data[B]["country"]}"

list_number = []
score = 0

print(art.logo)
compare_A = randomize_number()
list_number.append((compare_A))
wrong_answer = False
while not wrong_answer:
    compare_B = randomize_next_number(list_number)
    list_number.append((compare_B))
    print(compare(compare_A, art.vs, compare_B))
    valid_answer = False
    while not valid_answer:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_answer == 'A':
            if data[compare_A]["follower_count"] > data[compare_B]["follower_count"]:
                valid_answer = True
                score += 1
                print(art.logo)
                if score == 49:
                    print(f"You're right, current score: {score}")
                    print("You Won The Game!!")
                    wrong_answer = True
                else:
                    print(f"You're right, current score: {score}")
            else:
                valid_answer = True
                wrong_answer = True
                print("You're Wrong!")
                print(f"Your current score: {score}")
        elif user_answer == 'B':
            if data[compare_B]["follower_count"] > data[compare_A]["follower_count"]:
                valid_answer = True
                score += 1
                compare_A = compare_B
                print(art.logo)
                if score == 49:
                    print(f"You're right, current score: {score}")
                    print("You Won!!")
                    wrong_answer = True
                else:
                    print(f"You're right, current score: {score}")
            else:
                valid_answer = True
                wrong_answer = True
                print("You're Wrong!")
                print(f"Your current score: {score}")
        else:
            print("Invalid input. Please type 'A' or 'B'.")