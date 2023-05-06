import tkinter as tk

import text_const
from main import GamePlay
from lucy import Lucy


class MainWindow:
    def __init__(self, img1, img2, img3):
        self.root = tk.Tk()
        self.root.title("Q & A")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)

        self.bg1 = tk.PhotoImage(file=img1)
        self.bg2 = tk.PhotoImage(file=img2)
        self.bg3 = tk.PhotoImage(file=img3)

    def change_bg(self, mood=None):
        match mood:
            case "Ask":
                bg_label = tk.Label(self.root, image=self.bg1)
            case "Sad":
                bg_label = tk.Label(self.root, image=self.bg2)
            case _:
                bg_label = tk.Label(self.root, image=self.bg3)

        bg_label.place(x=-2, y=-2)

    @staticmethod
    def create_text(text):
        text_label = tk.Label(text=text, font=("Arial", 20), bg="#B22222", fg='#ffffff')
        text_label.place(relheight=0.30, relwidth=0.956, relx=0.022, rely=0.675)

    def create_button(self, *args, func):
        next_button = tk.Button(self.root, text="Next", font=("Arial", 20), bg="#B22222",
                                fg='#ffffff', command=lambda: func(*args))
        next_button.place(relheight=0.07, relwidth=0.2, relx=0.74, rely=0.9)

    def bindings(self):
        self.root.bind('a', lambda event: print("A was pressed"))

    @staticmethod
    def delete(element):
        element.destroy()

    def end(self):
        self.root.mainloop()


def great_txt(txt):
    for i in range(0, len(txt), 50):
        if i != 0:
            txt = txt[:i] + "\n" + txt[i:]
    return txt


class StartWin(MainWindow):
    def __init__(self, img1, img2, img3):
        super().__init__(img1, img2, img3)
        self.text_label1 = None
        self.text_label2 = None
        self.name1_entry = None
        self.name2_entry = None

        self.change_bg()
        self.create_text(text=great_txt(text_const.hello))
        self.create_button(func=self.create_entries)

        self.lucy_ins = Lucy(GamePlay.get_data())

    def create_entries(self):
        self.text_label1 = tk.Label(text="First team name", font=("Arial", 20), bg="#B22222", fg='#ffffff')
        self.text_label2 = tk.Label(text="Second team name", font=("Arial", 20), bg="#B22222", fg='#ffffff')
        self.name1_entry = tk.Entry(self.root, font=("Arial", 20), fg="#B22222")
        self.name2_entry = tk.Entry(self.root, font=("Arial", 20), fg="#B22222")

        self.name1_entry.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.3)
        self.name2_entry.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.5)
        self.text_label1.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.20)
        self.text_label2.place(relheight=0.08, relwidth=0.4, relx=0.54, rely=0.4)
        self.create_button(func=self.get_from_entries)

    def get_from_entries(self):
        self.lucy_ins.make_team(self.name1_entry.get(), 'a', self.name2_entry.get(), 'l')
        self.delete(self.root)


if __name__ == "__main__":
    my = StartWin("lucy1.png", "lucy2.png", "lucy3.png")
    my.end()
