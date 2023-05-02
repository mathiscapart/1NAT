from tkinter import *

global dessin, launch, balle1, move, launch, balle1, dx, dy
dessin = None
int = Tk()
int.geometry("1580x900")
exitpage = PhotoImage(file="image/button_exit.png")
titlepic = PhotoImage(file="image/title.png")
btn_play = PhotoImage(file="image/button_play.png")
level1_brick = PhotoImage(file="image/level1_brickfinal.png")
empty_brick = PhotoImage(file="image/vide.png")
state = 0

dx = 0
dy = 2


def move(*args):
    global state

    if state == 1:
        launch.destroy()
    state = 1
    global dx, dy
    dessin.move(balle1, dx, dy)
    int.after(10, move)
    # if dessin.coords(balle1)[3] >400:
    #    dy=-dy

    if dessin.coords(balle1)[3] < +10:
        dy = -dy

    elif dessin.coords(balle1)[2] < 0:
        dx = -dx

    elif dessin.coords(balle1)[2] > 500:
        dx = -dx

    # if dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3] + 100):
    #    int.destroy()
    if ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            (dessin.coords(platformbase)[3]) > dessin.coords(balle1)[3])) and (
            (dessin.coords(platformbase)[2] - 10) < dessin.coords(balle1)[2] < (
            dessin.coords(platformbase)[2] + 15)):
        dy = -dy
        dx = 2
    elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
            (dessin.coords(platformbase)[2] - 55) < dessin.coords(balle1)[2] < (
            dessin.coords(platformbase)[2] - 30)):
        dy = -dy
        dx = -2
    elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
            (dessin.coords(platformbase)[2] - 55) < dessin.coords(balle1)[2] < (
            dessin.coords(platformbase)[2])):
        dy = -dy
        dx = 0
    if dessin.coords(balle1)[3]>500:
        loose()

def moveplat(*args):
    if dessin.coords(platformbase)[2] < 500:
        dessin.move(platformbase, 20, 0)


def moveplat_rev(*args):
    if dessin.coords(platformbase)[2] > 40:
        dessin.move(platformbase, -20, 0)


def loose():
    dessin.destroy()

def game():
    global platformbase, dessin, launch, balle1
    dessin = Canvas(int, bg="black", width=500, height=400)
    balle1 = dessin.create_oval(5, 5, 15, 15, fill='white')
    launch = Button(int, image=btn_play, command=move)

    # brick = dessin.create_image(50, 50, image=level1_brick)
    # dessin.moveto(brick, 5, 5)

    platformbase = dessin.create_rectangle(80, 30, 20, 20, fill="blue")
    dessin.moveto(platformbase, 230, 300)
    dessin.moveto(balle1, 240, 20)
    int.bind("<Right>", moveplat)
    int.bind("<Left>", moveplat_rev)

    launch.pack(side=BOTTOM)
    dessin.pack()


def maingame():
    game()


Button(int, bg="black", command=maingame).pack()

int.mainloop()
