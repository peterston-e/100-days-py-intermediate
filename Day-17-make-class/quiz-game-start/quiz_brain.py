# todo quiz brain class
# attributes: question number = 0, question list
# methods: next_question

# create class
# add thee two attributes and the list is initialised when
# quizbrain in created by passing in the question bank

class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}. {question.text}. (True/False)?: ")
        # return user_answer
