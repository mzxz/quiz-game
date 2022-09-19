class QuizBrain:
    """
    Quiz brain class, asking questions, checking answers and end of the game
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        pass

    def next_question(self):
        pass

    def check_answer(self, user_answer, correct_answer):
        pass