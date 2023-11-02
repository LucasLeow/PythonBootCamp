from question_model import Question
from data import question_data
from quiz import Quiz
import os
from art import logo

question_bank = list()
for qns in question_data:
    question_bank.append(Question(qns['text'], qns['answer']))


play_again = True
while play_again:
    print(logo)
    os.system('cls')
    quiz_game = Quiz(question_bank)
    while(quiz_game.still_has_questions()):
        correct = quiz_game.ask_question()

        if not correct:
            while True:
                usr_choice = input('Play again? (y or n): ')
                if usr_choice.lower() == 'y':
                    break
                elif usr_choice.lower() == 'n':
                    play_again = False
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'")


print('Thank you for playing. Have a nice day!')