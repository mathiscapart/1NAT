from tkinter import *
from tkinter import ttk

def score():

    board_windows = Toplevel()
    board_windows.config(bg="white")
    board_windows.title("scoreboard")
    board_windows.resizable(height=False, width=False)

    board = ttk.Treeview(board_windows, columns=(1,2,3), height=5, show="headings")
    board.pack()

    board.heading(1, text="Place")
    board.heading(2, text="Pseudo")
    board.heading(3, text="Score")

    board.column(1, width=150)
    board.column(2, width=150)
    board.column(3, width=150)

    board.mainloop()