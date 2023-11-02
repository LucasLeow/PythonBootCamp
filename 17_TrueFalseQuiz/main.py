from question_model import Question
from data import question_data
from quiz import Quiz

question_bank = list()
for qns in question_data:
    question_bank.append(Question(qns['text'], qns['answer']))

quiz_game = Quiz(question_bank)
while(quiz_game.still_has_questions()):
    correct = quiz_game.ask_question()


