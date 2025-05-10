# open the starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

# open the invited_names.txt and convert it to list
with open("./Input/Names/invited_names.txt") as file_name:
    list_name = file_name.readlines()

for i in range(len(list_name)):
    # strip a space
    stripped_name = list_name[i].strip()
    # create a new letter with a custom file name and save it in ReadyToSend folder.
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
        # change the name
        new_letter = starting_letter.replace("[name]", stripped_name)
        final_letter.write(new_letter)
