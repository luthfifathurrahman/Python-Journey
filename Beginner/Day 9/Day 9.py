# Dictionary
food = {
    "fruit": "apple",
    "veggies": "spinach"
}

# retrieve an item from dictionary
print(food["fruit"])

# add an item to dictionary
food["drink"] = "water"
print(food)

# create an empty dictionary
empty_dict = {}

# wipe an existing dict
# food = {}
# print(food)

# edit an item in a dictionary
food["fruit"] = "watermelon"
print(food)

# how to loop through a dictionary
for key in food:
    print(key) # print the key
    print(food[key]) # print the value

# exercise
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Outstanding"

print(student_grades)

# Nesting
new_dict = {
    "key": "value"
}

nesting_dict = {
    "key": ["list1", "list2"],
    "key2": {"key_dict1": "value_dict1"}
}

# print list1
print(nesting_dict["key"][0])

# print value_dict1
print(nesting_dict["key2"]["key_dict1"])

# nested list
nested_list = ["a", "b", ["c", "d"]]

# print "d"
print(nested_list[2][1])

travel_log = {
    "france": {
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visits": 12
    },
    "germany": {
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 5
    }
}

# print stuttgart
print(travel_log["germany"]["cities_visited"][2])