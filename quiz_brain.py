class QuizBrain:
    """
    Quiz brain class, asking questions, checking answers and end of the game
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text}"
            f"(True/False): \n").lower()
        while user_answer not in ("true", "false"):
            print("\n")
            print('Please enter valid answer(True or False)')
            print("\n")
            print("Now try again!")
            user_answer = input(
                f"Q.{self.question_number}: {current_question.text}"
                f"(True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your curret score is: {self.score}/{self.question_number}")
        print("\n")
