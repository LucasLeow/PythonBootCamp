import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [str(i) for i in range(0, 10)]
symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(
    input("How many letters would you like in your password? \n"))
num_sym = int(input("How many symbols would you like? \n"))
num_num = int(input("How many numbers would you like?\n"))

password = []

for i in range(0, num_letters):
    password.append(letters[random.randint(0, len(letters)-1)])

for i in range(0, num_sym):
    password.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(0, num_num):
    password.append(numbers[random.randint(0, len(numbers)-1)])

random.shuffle(password)
print(f"Your generated password is {''.join(password)}")
