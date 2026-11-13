from pico2d import *
import Logo
import charecter 
import home

def Logo_Init():
    global schoolLogo
    schoolLogo = Logo.Logo()

def Init():
    global run_game
    global mainHome
    run_game = False
    mainHome = home.Home()



def update():
    pass

def drawScene():
    pass

def Process_event():
    pass

def draw_Logo():
    open_canvas(400, 250)
    clear_canvas()
    Logo_Init();
    schoolLogo.draw()
    update_canvas()
    delay(2)
    close_canvas()


def draw_home():
    while not run_game:
        clear_canvas()

        mainHome.ProcessEvent(run_game)

        mainHome.draw()

        update_canvas()

        delay(0.1)

#main

draw_Logo()

#draw_Logo()

open_canvas(1200, 800)

Init()

draw_home()

while run_game:
    clear_canvas()

    Process_event()

    update()

    drawScene()

    update_canvas()

    delay(0.1)

close_canvas