from questions_model import Question
from data import question_data
from quiz_logic import QuizLogic

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text = question_text, answer = question_answer)
    question_bank.append(new_question)

quiz = QuizLogic(question_list = question_bank)


while quiz.more_question():
    quiz.next_question()

print(f'You got {quiz.number_of_correct_answers}/{quiz.question_number} correct!')