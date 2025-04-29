# random module
import random

random_int = random.randint(1, 10)
print(random_int)

random_0_to_1 = random.random()
print(random_0_to_1)

random_0_to_10 = random.random() * 10 # you can not get 10
print(random_0_to_10)

random_float = random.uniform(1, 10) # you can get 10
print(random_float)

# heads or tail
random_head_tail = random.randint(0, 1)
if random_head_tail == 0:
    print("Head")
else:
    print("Tail")

# list
fruits = ["apple", "banana", "melon"]
print(fruits[0]) # show the first fruit in the list
print(fruits[-1]) # show the last fruit in the list

# change item in list
fruits[0] = "watermelon"
print(fruits)

# add item at the end of a list
fruits.append("apple")
print(fruits)

# extend a list
fruits.extend(["Dragon Fruit", "Orange"])
print(fruits)

# PRACTICE who will pay the bill
friends = ["alice", "bob", "charlie", "david", "emanuel"]
print(friends[random.randint(0, 4)])
print(friends[random.randint(0, len(friends) - 1)])
print(random.choice(friends))

# nested list
fruits = ["apple", "banana", "melon"]
vegies = ["spinach"]
food = [fruits, vegies]
print(food)