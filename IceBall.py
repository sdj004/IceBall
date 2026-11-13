from pico2d import *
import Logo
import charecter 
import home
import fightBack

def Logo_Init():
    global schoolLogo
    schoolLogo = Logo.Logo()

def mainHome_Init():
    global run_game
    global mainHome
    run_game = False
    mainHome = home.Home()

def fightSpace_Init():
    global FightBackground
    global player

    player = charecter.Charecter()
    FightBackground = fightBack.Background()

def update():
    global player
    player.update()

def drawScene():
    clear_canvas()

    FightBackground.draw()

    player.draw()

    update_canvas()

def Process_event(run_game):
    global player

    run_game = player.ProcessEvent(run_game)
    
    return run_game
        

def draw_Logo():
    open_canvas(400, 250)
    clear_canvas()
    Logo_Init()
    schoolLogo.draw()
    update_canvas()
    delay(2)
    close_canvas()


def draw_home():
    global run_game

    while not run_game:
        clear_canvas()

        run_game = mainHome.ProcessEvent(run_game)

        mainHome.draw()

        update_canvas()

        delay(0.1)

#main

draw_Logo()

#draw_Logo()

open_canvas(1200, 800)

mainHome_Init()

draw_home()

if run_game == True : 
    fightSpace_Init()
    print("enter fight map")

while run_game:

    run_game = Process_event(run_game)

    update()

    drawScene()

    delay(0.01)

close_canvas