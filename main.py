import text_const
from api_call import MakeApiCall
from validators import Replacer
from graphics.mainwin import *
import pygame


class GamePlay:

    def __init__(self):
        self.lucy_ins = None
        self.data = None

        self.play_music()

        self.data = self.get_data()
        self.graphic = StartWin("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png", self.data)
        self.graphic.end()
        self.lucy_ins = self.graphic.lucy_ins

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

        self.graphic = PlayWin("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png",
                               self.lucy_ins, self.data)
        self.graphic.end()

        self.lucy_ins.get_scores()


if __name__ == "__main__":
    new_game = GamePlay()
    new_game.start()
