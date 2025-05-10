import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# convert to dictionary
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# asked a word
word = input("Enter a word: ").upper()
# convert the letter in the word into NATO Phonetic Alphabet
output = [nato_dict[letter] for letter in word]
print(output)