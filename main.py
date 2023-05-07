from api_call import MakeApiCall
from validators import Replacer
from graphics.mainwin import *
import pygame


class GamePlay:

    def __init__(self):
        self.graphic = None
        self.lucy_ins = None
        self.data = None

        self.play_music()

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
        while True:
            self.data = self.get_data()
            for i in range(len(self.data)):
                print(self.data[i]["correct_answer"])

            self.graphic = StartWin("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png",
                                    "graphics/main_lucy.png", self.data, "graphics/PLAY.png")
            self.graphic.end()
            self.lucy_ins = self.graphic.lucy_ins

            self.graphic = PlayWin("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png",
                                   "graphics/main_lucy.png", self.lucy_ins, self.data)
            self.graphic.end()

            self.graphic = EndWIn("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png",
                                  "graphics/main_lucy.png", self.lucy_ins)
            self.graphic.end()
            if not self.graphic.continue_game_bool:
                break


if __name__ == "__main__":
    try:
        new_game = GamePlay()
        new_game.start()
    except Exception as e:
        print(e)

