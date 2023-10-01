import random
import Day7_HangmanArt as hangArt
import Day7_HangmanWords


def playHangman():
    # Setup
    chosen_word = random.choice(Day7_HangmanWords.countries).lower()
    display = ["_" for i in chosen_word]
    entered_before = []
    mistakes = 6
    play_again = True


    # UI
    print("Welcome to Country Guess Hangman")
    print(hangArt.logo)
    print("Guess the following Country: ")
    print(' '.join(display))

    # Gameplay
    while ("_" in display):

        if mistakes < 0:
            break

        user_guess = input("Guess a letter: ").lower()
        if len(user_guess) > 1:
            print("Please enter only 1 letter!")
            continue

        if (user_guess in entered_before):
            print("You have already guessed this letter!")
            continue

        entered_before.append(user_guess)

        if (user_guess in chosen_word):
            for i in range(len(chosen_word)):
                if (user_guess == chosen_word[i]):
                    display[i] = user_guess
            print(' '.join(display))
        else:
            print(hangArt.stages[mistakes])
            print(' '.join(display))
            mistakes -= 1

    if mistakes < 0:
        print(f"You lose! The answer was {chosen_word}")

    else:
        print("You win!")

playagain = True

while playagain:
    playHangman()

    while True:
        usr_input = input("Play again? (Y / N): ").lower()
        if len(usr_input) > 1:
            print("Invalid input, enter Y or N")
            continue
        if (usr_input not in ['y', 'n']):
            print("Invalid input, enter Y or N")
            continue
        else:
            if usr_input == 'y':
                playagain = True
                break
            else:
                playagain = False
                print("Thank you for playing!")
                break
