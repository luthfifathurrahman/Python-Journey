# For Loop
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Exercise: sum score
student_score = [10, 20 , 30, 40, 50]
total_exam_score = sum(student_score)
sum = 0
for score in student_score:
    sum += score
print(sum)

# Exercise: max score using for loops
student_score = [10, 20 , 30, 40, 50]
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)

# range
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# range using step
sum = 0
for number in range(1, 101, 3):
    sum += number
print(sum)

# Exercise: FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)