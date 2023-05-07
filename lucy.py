class Lucy:

    def __init__(self, data) -> None:
        self.team_b = None
        self.team_a = None
        self.turn = None
        self.data = data
        self.mood = None

    def make_team(self, name1, button1, name2, button2):
        self.team_a = {'name': name1, 'button': button1, 'score': 0}
        self.team_b = {'name': name2, 'button': button2, 'score': 0}
        print(f"Team {name1} and team {name2} were created")
        return self.team_a, self.team_b

    @staticmethod
    def correct_ans(team):
        team['score'] += 2

    @staticmethod
    def incorrect_ans(team):
        team['score'] -= 2

    def get_scores(self):
        return self.team_a['score'], self.team_b['score']
