# Paths
letter_path = 'Input/Letters/starting_letter.txt'
names_path = 'Input/Names/invited_names.txt'
output_path = 'Output/ReadyToSend/'

with open(names_path, 'r') as name_file:
    names = name_file.readlines()
    cleaned_names = [name.strip() for name in names]

    for name in cleaned_names:
        with open(letter_path, 'r') as letter:
            all_lines = letter.readlines()
            all_lines[0] = all_lines[0].replace('[name]', name)
            all_lines[-1] = all_lines[-1].replace('Angela', 'Lucas')

            with open(output_path + f'letter_for_{name}.txt', 'w') as output_file:
                output_file.writelines(all_lines)
