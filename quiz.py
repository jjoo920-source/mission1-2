class Quiz:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def check_answer(self, user_answer):
        # 정답 텍스트와 일치하거나
        if self.answer == user_answer:
            return True
        # 입력값이 정답 텍스트를 포함하거나
        if self.answer in user_answer:
            return True
        # 번호로 입력했을 때 - 해당 번호의 옵션이 정답을 포함하면 정답
        for option in self.options:
            if option.startswith(user_answer) and self.answer in option:
                return True
        return False