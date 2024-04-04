from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item['question']
    answer = item['correct_answer']
    new_list = Question(text, answer)
    question_bank.append(new_list)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}")



















