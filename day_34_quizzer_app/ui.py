from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # specifying quiz_brain is of Quiz brain datatype during initialization

        self.quiz = quiz_brain   # this has access to every method and attributes in quiz brain class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("ariel", 15, "italic"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text((150, 125),
                                                     text="some question text", fill=THEME_COLOR,
                                                     font=("ariel", 15, "italic"), width=280)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.clicked_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.clicked_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # background will be always white when going to new question
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")   # updating the score
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_true(self):
        #  self.quiz can access quiz brain
        self.give_feedback(self.quiz.check_answer("True"))

    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
