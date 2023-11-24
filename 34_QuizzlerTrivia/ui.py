from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
QNS_FONT = ('Ariel', 12, 'italic')
PADDING = 20

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quizbrain = quizbrain
        self.usr_ans = None
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        # Question Text
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT) # for question
        self.canvas.configure(bg='white')
        self.qns_text = self.canvas.create_text(
            (CANVAS_WIDTH/2, CANVAS_HEIGHT/2),
            width=CANVAS_WIDTH-PADDING,
            text="",
            fill=THEME_COLOR,
            font=QNS_FONT)

        self.canvas.grid(row=1, column=0, columnspan=2, padx=PADDING, pady=PADDING)

        # Buttons
        tick_img = PhotoImage(file='images/true.png') # 100 x 97
        x_img = PhotoImage(file='images/false.png') # 100 x 97

        self.tick_btn = Button(image=tick_img, highlightthickness=0, command=self.true_btn_clicked)
        self.x_btn = Button(image=x_img, highlightthickness=0, command=self.false_btn_clicked)

        self.tick_btn.grid(row=2, column=0, padx=PADDING, pady=PADDING)
        self.x_btn.grid(row=2, column=1, padx=PADDING, pady=PADDING)

        # Score
        self.score_text = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 12, 'normal'))
        self.score_text.grid(row=0, column=1, padx=PADDING, pady=PADDING)

        self.get_next_qns()

        self.window.mainloop()

    def get_next_qns(self):
        self.canvas.config(bg='white')
        if self.quizbrain.still_has_questions():
            self.score_text.config(text=f'Score: {self.quizbrain.score}')
            q_text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.qns_text, text=q_text)
        else:
            self.canvas.itemconfig(self.qns_text, text="END OF QUIZ")
            self.tick_btn.config(state='disabled')
            self.x_btn.config(state='disabled')

    def true_btn_clicked(self):
        if self.quizbrain.still_has_questions():
            is_right = self.quizbrain.check_answer('True')
            self.give_feedback(is_right)

    def false_btn_clicked(self):
        if self.quizbrain.still_has_questions():
            is_right = self.quizbrain.check_answer('False')
            self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='#76EE00')
        else:
            self.canvas.configure(bg='coral1')
        self.window.after(1000, self.get_next_qns)

