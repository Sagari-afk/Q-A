from team import Team

import random


class Lucy:

    def __init__(self, data) -> None:
        self.team_b = None
        self.team_a = None
        self.turn = None
        self.data = data
        self.mood = None

    def make_team(self, name1, button1, name2, button2):
        self.team_a = Team(name=name1,
                           button=button1)
        self.team_b = Team(name=name2,
                           button=button2)
        print(f"Team {name1} and team {name2} were created")
        return self.team_a, self.team_b

    def ask_question(self, i):
        self.mood = "Ask"
        return self.data[i]["question"], self.mood

    def show_answers(self, i):
        random.shuffle(self.data[i]["all_answers"])

    def ans_check(self, i):
        team_answer = input("Your answer is --> ")
        if team_answer == self.data[i]["correct_answer"]:
            self.turn.correct_ans(self.data[i]["type"])
        else:
            self.turn.incorrect_ans(self.data[i]["type"])
            self.mood = "Sad"
        return self.mood

    def get_scores(self):
        return self.team_a.scores, self.team_b.scores
