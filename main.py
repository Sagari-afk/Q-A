import text_const
from api_call import MakeApiCall
from validators import Replacer
from lucy import Lucy
from graphics.mainwin import *
import pygame

import time


class GamePlay:

    def __init__(self):
        self.data = None
        self.graphic = MainWindow("graphics/lucy1.png", "graphics/lucy2.png", "graphics/lucy3.png")

    @staticmethod
    def music():
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

        self.music()
        self.graphic.change_bg(None)
        lucy_ins = Lucy(self.get_data())

        self.graphic.create_text(text=great_txt(text_const.hello))
        while not self.graphic.clicked:
            self.graphic.create_button(func=self.graphic.button_was_clicked)

        self.graphic.change_bg("Ask")
        self.graphic.clicked = False

        while not self.graphic.clicked:
            self.graphic.create_button(func=self.graphic.button_was_clicked)
        self.graphic.create_entries()
        self.graphic.clicked = False

        while not self.graphic.clicked:
            self.graphic.create_button(func=self.graphic.button_was_clicked)
        self.graphic.get_from_entries()

        print(self.graphic.name1_entry, self.graphic.name2_entry)

        # lucy_ins.make_team(self.graphic.name1, button1, self.graphic.name2, button2)
        #
        # time.sleep(3)
        #
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
