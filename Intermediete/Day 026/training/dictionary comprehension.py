# dictionary comprehension
# cheat code: new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

import random

# cheat code: new_dict = {new_key:new_value for item in list}
names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
students_scores = {name:random.randint(1, 100) for name in names}
print(students_scores)

# cheat code: new_dict = {new_key:new_value for (key,value) in dict.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score > 50}
print(passed_students)

# exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# exercise 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)