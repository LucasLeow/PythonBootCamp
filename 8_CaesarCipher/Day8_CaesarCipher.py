from Day8_caesarArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(msg, shift, direction):
    end_text = ""
    if (direction == "decode"):
        shift *= -1
    for char in msg:
        if (char in alphabet):
            position = alphabet.index(char)
            new_position = position + (shift % 26)
            if (new_position > len(alphabet) - 1):
                overlap = new_position - len(alphabet)
                end_text += alphabet[overlap]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


print(logo)
while (True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message \n").lower()
    shift = int(input("Enter shift number: \n"))

    caesar(msg=text, shift=shift, direction=direction)
    choice = input("Continue program? (Y / N)\n").lower()
    if (choice == "y"):
        continue
    else:
        print("Goodbye!")
        break
