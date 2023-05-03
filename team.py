class Team:

    def __init__(self, name: str, button, score: int = 0):
        self.name = name
        self.score = score
        self.button = button

    def correct_ans(self, question_type):
        if question_type == "multiple":
            self.score += 5
        else:
            self.score += 3

    def incorrect_ans(self, question_type):
        if question_type == "multiple":
            self.score -= 3
        else:
            self.score -= 2
