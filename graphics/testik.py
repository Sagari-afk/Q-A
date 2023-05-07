import tkinter as tk


root = tk.Tk()
root.title("Q & A")
root.geometry("800x600")
root.resizable(width=False, height=False)

root.bind('a', lambda event: print("A was pressed"))
root.bind('b', lambda event: print("B was pressed"))
root.unbind('a')


root.mainloop()
