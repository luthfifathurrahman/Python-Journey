# list comprehension
numbers = [1, 2, 3]
new_list = []
for number in numbers:
    new_number = number + 1
    new_list.append(new_number)
print(new_list)

# we can make it short like this
numbers = [1, 2, 3]
# cheat code: new_list = [new_item for item in list]
new_list_short = [number + 1 for number in numbers]
print(new_list_short)

name = "Luthfi"
new_list = [letter for letter in name]
print(new_list)

new_list_number = [number * 2 for number in range(1, 5)]
print(new_list_number)

# conditional list comprehension
# cheat code: new_list = [new_item for item in list if condition]
names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
short_names = [name for name in names if len(name) < 5 ]
upper_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_names)

# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# exercise 2
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)

# exercise 3
with open("file1.txt") as file1:
    int_stripped_file1 = [int(lines.strip()) for lines in file1.readlines()]

with open("file2.txt") as file2:
    int_stripped_file2 = [int(lines.strip()) for lines in file2.readlines()]

result = [number for number in int_stripped_file1 if number in int_stripped_file2]

print(result)
