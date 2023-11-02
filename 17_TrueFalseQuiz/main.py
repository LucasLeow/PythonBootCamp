from question_model import Question
from data import question_data

question_bank = list()
for qns in question_data:
    question_bank.append(Question(qns['text'], qns['answer']))


