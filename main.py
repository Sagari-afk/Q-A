import text_const
from api_call import MakeApiCall
from validators import Replacer
from lucy import Lucy
from graphics.mainwin import *
import pygame


class GamePlay:

    def __init__(self):
        self.data = None
        self.graphic = StartWin("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png")

    @staticmethod
    def play_music():
        pygame.init()
        pygame.mixer.music.load("lofi.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.05)

    @staticmethod
    def get_data():
        api_call = MakeApiCall({"amount": 10})
        raw_data = api_call.get_data("https://opentdb.com/api.php")
        val = Replacer(raw_data)
        data = val.replace_special_symbols()
        return data

    def start(self):

        self.play_music()

        self.graphic.end()

        # for i in range(len(self.data)):
        #     lucy_ins.ask_question(i)
        #     time.sleep(2)
        #
        #     lucy_ins.show_answers(i)
        #
        #     print(self.data[i]["all_answers"])
        #
        #     time.sleep(5)
        #     lucy_ins.ans_check(i)
        #
        # lucy_ins.get_scores()
        self.graphic.end()


if __name__ == "__main__":
    new_game = GamePlay()
    new_game.start()
