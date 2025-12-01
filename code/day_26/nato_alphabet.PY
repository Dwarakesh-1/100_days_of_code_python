# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_loop = True
while is_loop:
    word = input("Enter a word: ").upper()
    if word == "0":
        print("Thank you for using NATO conversion")
        is_loop = False
    else:
        output_list = [phonetic_dict[letter] for letter in word]
        print(f"Your {word} in NATO is {output_list}")
