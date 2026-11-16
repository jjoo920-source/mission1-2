class Quiz:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def check_answer(self, user_answer):
        return self.answer == user_answer