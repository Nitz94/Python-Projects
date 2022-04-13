from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


# question text is value of "text" key from question dictionary which is in question data.also applicable  for "answer"
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # text and answer stored inside Question object
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
