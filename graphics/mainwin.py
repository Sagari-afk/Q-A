import tkinter as tk                            # graphical user interface
from textwrap import wrap                       # module to automatically wrap text to a new line

import text_const                               # used to store text constants
from lucy import Lucy


def great_txt(txt):                             # a function that takes the text txt, wraps it on a new line if the
    txt = '\n'.join(wrap(txt, 50))              # length of the line exceeds 50 characters, and returns the new text.
    return txt


class MainWindow:
    """
    a class that initializes the main application window, sets its size,
    background images, and places controls (interface elements) on it.
    """
    def __init__(self, img1, img2, img3, img4):
        self.root = tk.Tk()
        self.root.title("Q & A")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)

        self.bg1 = tk.PhotoImage(file=img1)
        self.bg2 = tk.PhotoImage(file=img2)
        self.bg3 = tk.PhotoImage(file=img3)
        self.bg4 = tk.PhotoImage(file=img4)

        self.text_label1 = None
        self.text_label2 = None
        self.name1_entry = None
        self.name2_entry = None

    def change_bg(self, mood=None):  # changes the background image of the window depending on the passed mood argument.
        match mood:
            case "Ask":
                bg_label = tk.Label(self.root, image=self.bg1)
            case "Sad":
                bg_label = tk.Label(self.root, image=self.bg2)
            case "Start":
                bg_label = tk.Label(self.root, image=self.bg4)
            case _:
                bg_label = tk.Label(self.root, image=self.bg3)

        bg_label.place(x=-2, y=-2)

    def create_entries(self):       # creates labels and input fields for entering the names of two commands.
        self.text_label1 = tk.Label(text="First team name", font=("Arial", 20), bg="#B22222", fg='#ffffff')
        self.text_label2 = tk.Label(text="Second team name", font=("Arial", 20), bg="#B22222", fg='#ffffff')
        self.name1_entry = tk.Entry(self.root, font=("Arial", 20), fg="#B22222")
        self.name2_entry = tk.Entry(self.root, font=("Arial", 20), fg="#B22222")

        self.name1_entry.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.3)
        self.name2_entry.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.5)
        self.text_label1.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.20)
        self.text_label2.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.4)

    @staticmethod
    def create_text(text):      # creates a label with text.
        text_label = tk.Label(text=text, font=("Arial", 20), bg="#B22222", fg='#ffffff')
        text_label.place(relheight=0.30, relwidth=0.956, relx=0.022, rely=0.675)

    def create_button(self, *args, func):       # creates a button with the text "Next" and the given function
        next_button = tk.Button(self.root, text="Next", font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: func(*args))
        next_button.place(relheight=0.07, relwidth=0.2, relx=0.74, rely=0.9)

    def bindings(self, key):        # binds an event handler to a specific key press
        self.root.bind(key, lambda event: print("A was pressed"))

    def unbinding(self, key):       # removes the previously associated keypress event handler
        self.root.unbind(key)

    @staticmethod
    def delete(element):        # removes the element passed to it
        element.destroy()

    def end(self):          # launches the main application window
        self.root.mainloop()


class StartWin(MainWindow):
    def __init__(self, img1, img2, img3, img4, data, img5):
        # calls the constructor of the MainWindow
        super().__init__(img1, img2, img3, img4)

        self.data = data
        # creates an instance of the Lucy class
        self.lucy_ins = Lucy(self.data)
        # creates a new PhotoImage object, loading the image from the file
        self.img = tk.PhotoImage(file=img5)

        # line calls a method change_bg of the MainWindow
        self.change_bg("Start")
        self.b = tk.Button(self.root, image=self.img, font=("Arial", 20), command=lambda: self.start())
        self.b.place(relheight=0.14, relwidth=0.25, relx=0.54, rely=0.25)

    def start(self):    # method changes the background and creates a text and a button in the main window
        self.change_bg("Ask")
        self.create_text(text=great_txt(text_const.hello))
        self.create_button(func=self.create_entries)

    def create_entries(self):       # method calls the same-named method from the
        super().create_entries()    # superclass MainWindow and creates another button
        self.create_button(func=self.get_from_entries)

    def get_from_entries(self):
        # method uses an instance of the Lucy class to make
        # a team based on the values entered in two text entry
        # widgets (name1_entry and name2_entry) and then deletes
        # the entire window
        self.lucy_ins.make_team(self.name1_entry.get(), 'a', self.name2_entry.get(), 'l')
        self.delete(self.root)


class PlayWin(MainWindow):
    """
    responsible for creating the game window and handling the game logic.
    The __init__ method initializes several instance variables, sets the
    background and creates the initial text and button.
    """
    def __init__(self, img1, img2, img3, img4, lucy_ins, data):
        super().__init__(img1, img2, img3, img4)
        self.team = None
        self.b0 = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.clicked = None
        self.i = 0

        self.data = data
        self.lucy_ins = lucy_ins

        self.change_bg()
        self.create_text(text=great_txt(text_const.start_game.format(name1=self.lucy_ins.team_a["name"],
                                                                     name2=self.lucy_ins.team_b["name"])))
        self.create_button(data, self.i, func=self.play_play)

    def play_play(self, data, i):
        # method is called when the button is clicked and takes the question,
        # answers, and correct answer data from the data parameter and uses it
        # to create the next question. It binds the 'a' and 'l' keys to a lambda
        # function that calls the ask method with the appropriate team (team a or team b)

        question = data[i]["question"]
        answers = data[i]["all_answers"]
        correct_answer = data[i]["correct_answer"]

        self.root.bind('a', lambda event: self.ask(question, answers, correct_answer, 'a'))
        self.root.bind('l', lambda event: self.ask(question, answers, correct_answer, 'l'))

        print(i)

    def ask(self, question, answers, correct_answer, key):
        # takes the question, answers, and correct answer as parameters,
        # along with a key that specifies which team is answering. It creates
        # buttons for each answer, binds the buttons to the was_clicked method,
        # and places them on the window

        if key == 'a':
            self.team = self.lucy_ins.team_a
        if key == 'l':
            self.team = self.lucy_ins.team_b

        self.create_text(text=great_txt(question))
        if len(answers) == 4:
            self.b0 = tk.Button(self.root, text=answers[0], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b0, answers, correct_answer))
            self.b1 = tk.Button(self.root, text=answers[1], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b1, answers, correct_answer))
            self.b2 = tk.Button(self.root, text=answers[2], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b2, answers, correct_answer))
            self.b3 = tk.Button(self.root, text=answers[3], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b3, answers, correct_answer))
            self.b2.place(relheight=0.075, relwidth=0.5, relx=0.44, rely=0.4)
            self.b3.place(relheight=0.075, relwidth=0.5, relx=0.44, rely=0.5)
        else:
            self.b0 = tk.Button(self.root, text=answers[0], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b0, answers, correct_answer))
            self.b1 = tk.Button(self.root, text=answers[1], font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: self.was_clicked(self.b1, answers, correct_answer))

        self.b0.place(relheight=0.075, relwidth=0.5, relx=0.44, rely=0.2)
        self.b1.place(relheight=0.075, relwidth=0.5, relx=0.44, rely=0.3)

    def was_clicked(self, b, answers, correct_answer):
        # is called when a button is clicked and sets the clicked
        # instance variable to the index of the button that was clicked.
        # It checks if the clicked answer is correct and updates the score
        # and the background of the window accordingly. If there are more
        # questions to ask, it calls the play_play method with the next
        # question index, otherwise it unbinds the keys and deletes the window

        if b == self.b0:
            self.clicked = 0
        if b == self.b1:
            self.clicked = 1
        if b == self.b2:
            self.clicked = 2
        if b == self.b3:
            self.clicked = 3

        if answers[self.clicked] == correct_answer:
            self.lucy_ins.correct_ans(self.team)
            self.change_bg()
            self.create_text(text=great_txt("Super!! It was a correct answer"))
        else:
            self.lucy_ins.incorrect_ans(self.team)
            self.change_bg('Sad')
            self.create_text(text=great_txt("I`m sorry but you are wrong((((((((("))

        if self.i < 9:
            self.i += 1
            self.play_play(self.data, self.i)
        else:
            self.unbinding('a')
            self.unbinding('l')
            self.delete(self.root)


class EndWIn(MainWindow):
    def __init__(self, img1, img2, img3, img4, lucy_ins):
        super().__init__(img1, img2, img3, img4)

        self.continue_game_bool = None
        self.change_bg("Ask")

        # Create text on the screen with the end game scores
        self.create_text(text=great_txt(text_const.end_game.format(name1=lucy_ins.team_a["name"],
                                                                   score1=lucy_ins.team_a["score"],
                                                                   name2=lucy_ins.team_b["name"],
                                                                   score2=lucy_ins.team_b["score"])))

        # Save the instance of the Lucy class for later use
        self.lucy_ins = lucy_ins

        # Create two buttons with text, background color and font size
        self.b0 = tk.Button(self.root, text="Play again", font=("Arial", 20), bg="#B22222",
                            fg='#ffffff', command=lambda: self.continue_game(True))
        self.b1 = tk.Button(self.root, text="Finish", font=("Arial", 20), bg="#B22222",
                            fg='#ffffff', command=lambda: self.continue_game(False))

        # Place the buttons on the screen with relative position and size
        self.b0.place(relheight=0.075, relwidth=0.4, relx=0.54, rely=0.2)
        self.b1.place(relheight=0.075, relwidth=0.4, relx=0.54, rely=0.3)

    # Function to set the value of continue_game_bool to either True or False
    def continue_game(self, want):
        self.continue_game_bool = want

        # Delete everything on the screen
        self.delete(self.root)