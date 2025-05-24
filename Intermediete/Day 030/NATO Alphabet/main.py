import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# convert to dictionary
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()