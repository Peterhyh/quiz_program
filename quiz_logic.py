class QuizLogic:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.number_of_correct_answers = 0

    def more_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} ')
        if user_answer == current_question.answer:
            print('You got it right!')
            self.number_of_correct_answers += 1
        else:
            print('Wrong')
        print(f'The correct answer was: {current_question.answer}\n\n')
