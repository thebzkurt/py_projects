import pandas as pd
from pandas.io.formats.format import return_docstring

df = pd.read_csv("nato_phonetic_alphabet.csv")

new_dic = {row.letter:row.code for (index, row) in df.iterrows()}

while True:
    try:
        input_name = input("Enter the name: ").upper()
        input_list = [new_dic[letter] for letter in input_name]
    except KeyError as e:
        print(f'Error: {KeyError}, Only letters in the alphabet please.')
    else:
        print(input_list)
        break
