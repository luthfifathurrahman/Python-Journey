# # read a file using Absolute File Path
# with open("F:\\My Data\\4. Data Project\\UdemyPython\\Intermediate\\Day 024\\training\\File Path\\data\\file.txt") as file:
#     contents = file.read()
#     print(contents)

# read a file using Relative File Path
with open("data/file.txt") as file:
    contents = file.read()
    print(contents)

# # write a file
# with open("file.txt", mode="w") as file:
#     file.write("New text.")

# # append a file
# with open("file.txt", mode="a") as file:
#     file.write("New text.")

# # create a new file
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")