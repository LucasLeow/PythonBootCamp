class Quiz:
    def __init__(self, qns_bank):
        self.question_number = 0
        self.question_list = qns_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def ask_question(self):
        validation_flag = True
        while validation_flag:
            usr_answer = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)? : ")
            if usr_answer.lower() in ['true', 'false']:
                break
            else:
                print('Invalid input. Please enter true or false only')
        correct = self.check_ans(usr_answer)
        if correct:
            self.question_number += 1
            print('You got it right!')
            print(f'Current score: {self.score}')
            return True
        else:
            print("That's wrong")
            print(f'Final score: {self.score}')
            self.question_number = len(self.question_list)
            return False

    def check_ans(self, usr_ans):
        if usr_ans.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            return True
        return False