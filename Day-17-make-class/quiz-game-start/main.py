from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

# create question bank
question_bank = []

# loop through data
# extract question and answer
# create question object
# add to question bank
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)
# print(question_bank[0].text)
# print(question_bank[0].answer)
# So, now it's a list of objects, it's easier to access it.
# If it was a list of dictionaries, you would have to use strings
# to access all the keys and easy to make mistakes.
# Now you can use the dot notation and get the helper box pop-up
# And you still have access to all the list modules also.


# Todo ask user the question
# todo check the answer
# todo check if at the end of the quiz
quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
