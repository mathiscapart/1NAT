from tkinter import *
import game


menu = Tk()
menu.config(bg="white")
menu.attributes("-fullscreen", True)
menu.title("Menu")

title = PhotoImage(file="image/title.png")
start = PhotoImage(file="image/button_play.png")
exit = PhotoImage(file="image/button_exit.png")

def on_game():
    game.menu_start_game()

def exit_windows():
    menu.destroy()

name_game = Label(menu, image=title, bg="white")
name_game.pack(anchor="center", pady=100)

start_game = Button(menu, image=start, command=on_game, relief="flat", borderwidth=0, bg="white")
start_game.pack(pady=10)
btn_exit = Button(menu, image=exit, command=exit_windows, relief="flat", borderwidth=0, bg="white")
btn_exit.pack(ipadx=20, pady=5)

menu.mainloop()