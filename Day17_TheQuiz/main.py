# Day 17 - the Benefits of OOP
# Day 17 - Project: The Quiz

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

new_quiz.end_of_the_game()