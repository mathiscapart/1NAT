from tkinter import *
from tkinter import ttk
import mysql.connector


def score():

    board_windows = Toplevel()
    board_windows.config(bg="white")
    board_windows.title("scoreboard")

    board = ttk.Treeview(board_windows, columns=(1,2,3), height=5, show="headings")
    board.pack()

    board.heading(1, text="Place")
    board.heading(2, text="Pseudo")
    board.heading(3, text="Score")

    try:
        connection = mysql.connector.connect(
            host="192.168.25.169",
            port=3306,
            user='root',
            password='EcoleIT123!',
            database='score'
        )
    except mysql.connector.Error as e:
        print("Erreur lors de la connexion à la base de données :", e)
        exit()

    cursor = connection.cursor()
    query = "SELECT * FROM score ORDER BY score DESC"
    cursor.execute(query)

    place = 0
    for i in cursor:
        place+=1
        place_label = Label(board, text=place)
        place_label.grid(row=place, column=0)
        pseudo_label = Label(board, text=i[1])
        pseudo_label.grid(row=place, column=1)
        score_label = Label(board, text=i[2])
        score_label.grid(row=place, column=2)
        date_label = Label(board, text=i[3])
        date_label.grid(row=place, column=3)


    board.column(1, width=150)
    board.column(2, width=150)
    board.column(3, width=150)

    board.mainloop()
    cursor.close()
    connection.close()