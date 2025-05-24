# # # handling error and exceptions
# #filenotfound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is an error that i made up")

# # raise example
# height = float(input("height: "))
# weight = float(input("weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight/height ** 2
# print(bmi)


# #keyerror
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]
#
# #indexerror
# fruits = ["banana", "apple", "pear"]
# fruit = fruits[3]
#
# #typeerror
# text = "abc"
# print(text + 5)