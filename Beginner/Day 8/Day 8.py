# function with input
def greet():
    print("hello")
    print("halo")
    print("hola")

def greet_with_name(name):
    print(f"hello {name}")
    print(f"halo {name}")
    print(f"hola {name}")

greet()
greet_with_name("luthfi")

# Exercise
def life_in_weeks(your_age):
    age_left = 90 - your_age
    week_left = age_left * 52
    print(f"You have {week_left} weeks left.")

life_in_weeks(56)

# function with more than 1 input
def greet_with(name, location):
    print(f"halo {name}")
    print(f"what is it like in {location}?")

# positional argument
greet_with("luthfi", "nowhere")
# keyword argument
greet_with(location="nowhere", name="luthfi")

# Exercise
def calculate_love_score(name1, name2):
    both_name = (name1 + name2).lower()
    true_score = 0
    love_score = 0
    for index in range(len(both_name)):
        if both_name[index] in "true":
            true_score += 1

        if both_name[index] in "love":
            love_score += 1
    total_score = true_score * 10 + love_score
    print(total_score)

calculate_love_score("Angela Yu", "Jack Bauer")
