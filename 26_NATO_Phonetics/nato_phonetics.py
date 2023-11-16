import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {r.letter: r.code for (i, r) in df.iterrows()}

while True:
    usr_input = input('Enter a word (end to quit): ').upper()
    if usr_input == 'EXIT':
        break
    nato_equivalent = [nato_dict[char] for char in usr_input]
    print(nato_equivalent)

print('Thank you and have a nice day')