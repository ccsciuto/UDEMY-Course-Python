from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial",20,"italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        right_img = PhotoImage(file="right.png")
        self.check_button = Button(image=right_img, highlightthickness=0, bg="grey", borderwidth=0, command=self.answer_true)
        self.check_button.grid(column=0, row=2)
        wrong_img = PhotoImage(file="wrong.png")
        self.ex_button = Button(image=wrong_img, highlightthickness=0, bg="grey", borderwidth=0, command=self.answer_false)
        self.ex_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.ex_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)