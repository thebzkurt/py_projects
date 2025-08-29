import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

new_list = {row.letter:row.code for (index, row) in df.iterrows()}

input_name = input("Enter the name: ").upper()
input_dic = [new_list[letter] for letter in input_name]
print(input_dic)

