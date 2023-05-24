from tkinter import *

global dessin, launch, balle1, dx, dy, brick1, vie_num, btnvie, tab_brick, tab_live_brick, numbrick
dessin = None
int = Tk()
int.geometry("1580x900")
exitpage = PhotoImage(file="image/button_exit.png")
titlepic = PhotoImage(file="image/title.png")
btn_play = PhotoImage(file="image/button_play.png")
level1_brick = PhotoImage(file="image/level1_brickfinal.png")
empty_brick = PhotoImage(file="image/vide.png")
state = 0

def create_life():
    global tab_life
    tab_life = []
    for i in range(5):
        life = dessin.create_oval(60, 60, 60, 60, fill="red")
        dessin.moveto(life, 300, 400 + (i * 60))
        tab_life.append(life)

def create_brick():
    global tab_brick,tab_live_brick
    tab_brick = []
    tab_live_brick = []
    for x in range(9):
        for i in range(9):
            tab_live_brick.append(3)
            brick = dessin.create_rectangle(i * 55, x * 20, (i + 1) * 55, (x + 1) * 20, fill="pink")
            tab_brick.append(brick)

def move(*args):
    global state, dessin, dx, dy, vie_num, tab_brick, numbrick,launch,tab_live_brick

    dessin.move(balle1, dx, dy)
    int.after(10, move)

    if dessin.coords(balle1)[3] < 10:
        dy = -dy
    elif dessin.coords(balle1)[2] < 20:
        dx = -dx
    elif dessin.coords(balle1)[2] > 490:
        dx = -dx
    elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            (dessin.coords(platformbase)[3]) > dessin.coords(balle1)[3])) and (
            (dessin.coords(platformbase)[2] - 10) < dessin.coords(balle1)[2] < (dessin.coords(platformbase)[2] + 15)):
        dy = -dy
        dx = 2
    elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
            (dessin.coords(platformbase)[2] - 55) < dessin.coords(balle1)[2] < (dessin.coords(platformbase)[2] - 30)):
        dy = -dy
        dx = -2
    elif ((dessin.coords(balle1)[3] > (dessin.coords(platformbase)[3]) - 10) and (
            dessin.coords(balle1)[3] < (dessin.coords(platformbase)[3]))) and (
            (dessin.coords(platformbase)[2] - 50) < dessin.coords(balle1)[2] < (dessin.coords(platformbase)[2] + 10)):
        dy = -dy
        dx = 0

    if dessin.coords(balle1)[3] > 500:
        vie_num = vie_num - 1
        dessin.moveto(balle1, 250, 250)
        dx = 0
        if vie_num == 0:
            loose()

    for brick in tab_brick:
        brick_index = tab_brick.index(brick)
        brick_collision = dessin.find_overlapping(*dessin.coords(brick))
        if len(brick_collision) > 1:
            for item in brick_collision:
                if item == balle1:
                    dy = -dy
                    tab_live_brick[brick_index] -=1
                    if tab_live_brick[brick_index] == 2 :
                        dessin.itemconfig(brick,fill="purple")

                    elif tab_live_brick[brick_index] == 1:
                        dessin.itemconfig(brick,fill="yellow")
                    if tab_live_brick[brick_index] == 0 :
                        dessin.delete(brick)
                        tab_brick.remove(brick)
                        numbrick -= 1
                    break
        if numbrick <= 0:
            victory_event()

def moveplat(*args):
    if dessin.coords(platformbase)[2] < 500:
        dessin.move(platformbase, 20, 0)

def moveplat_rev(*args):
    if dessin.coords(platformbase)[0] > 0:
        dessin.move(platformbase, -20, 0)

def victory_event():
    dessin.destroy()

def loose():
    global vie_num
    dessin.destroy()

def restart_game():
    global state, dessin, launch, balle1, dx, dy, brick1, vie_num, btnvie, tab_brick, numbrick

    state = 0
    dessin = None
    launch = None
    balle1 = None
    dx = 0
    dy = 0
    brick1 = None
    vie_num = 0
    btnvie = None
    tab_brick = []
    numbrick = 0

    game()

def game():
    global platformbase,dessin, launch, balle1, dx, dy, brick1, vie_num, btnvie,tab_brick, numbrick
    dessin = Canvas(int, bg="black", width=500, height=400)
    dx = 0
    dy = 2
    balle1 = dessin.create_oval(5, 5, 15, 15, fill='white')
    create_life()
    create_brick()

    numbrick = 81
    vie_num = 3
    platformbase = dessin.create_rectangle(80, 30, 20, 20, fill="red")
    border_left = dessin.create_rectangle(30, 500, 20, 20, fill="cyan")
    border_right = dessin.create_rectangle(30, 500, 20, 20, fill="cyan")

    dessin.moveto(platformbase, 220, 350)
    dessin.moveto(balle1, 250, 250)
    dessin.moveto(border_left, 0, 0)
    dessin.moveto(border_right, 491, 0)

    int.bind("<Right>", moveplat)
    int.bind("<Left>", moveplat_rev)

    dessin.pack()



Button(int,bg="blue",text="restart",command=restart_game).pack(anchor=SE)
int.bind("a", move)
Button(int, bg="black", command=game).pack()

int.mainloop()
