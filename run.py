import sys
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


def play():

    quiz = QuizBrain(question_bank)
    try:
        while quiz.still_has_questions:
            quiz.next_question()
    except IndexError:
        print("The end")
        print("You have completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")
        print("\n")
        again = input("Do you want to play again(type y or,"
                      " press any letter or number to exit): \n"
                      ).lower()
        while again == "y":
            print("\n")
            play()
        else:
            sys.exit()


play()