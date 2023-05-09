from api_call import MakeApiCall
from validators import Replacer
from graphics.mainwin import *
import pygame


class GamePlay:     # responsible for initializing the game and playing it.

    def __init__(self):
        # The constructor of GamePlay initializes graphic, lucy_ins,
        # and data variables as None. play_music() function is called to play the background music.
        self.graphic = None
        self.lucy_ins = None
        self.data = None

        self.play_music()

    @staticmethod
    def play_music():
        # initializes the Pygame module and plays the music loaded from the file
        pygame.init()
        pygame.mixer.music.load("lofi.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.05)

    @staticmethod
    def get_data():
        # retrieve data from the API using MakeApiCall and Replacer classes.
        # amount is the number of questions to retrieve from the API
        api_call = MakeApiCall({"amount": 10})
        raw_data = api_call.get_data("https://opentdb.com/api.php")
        val = Replacer(raw_data)
        data = val.replace_special_symbols()
        return data

    def start(self):
        # This function runs the game by first retrieving the data using
        # the get_data() method. Then it initializes StartWin, PlayWin,
        # and EndWIn classes with the appropriate parameters. Finally,
        # the end() method of each class is called to run the game.
        # If continue_game_bool is False, the game ends; otherwise, it continues running.
        while True:
            self.data = self.get_data()
            for i in range(len(self.data)):
                print(f"{self.data[i]['correct_answer']} ----> {self.data[i]['difficulty']}")

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


if __name__ == "__main__":      # statement is used to check whether the current module is being run as the main program
    try:
        new_game = GamePlay()
        new_game.start()
    except Exception as e:      # If an exception occurs, it is caught by the except block
        print(e)
