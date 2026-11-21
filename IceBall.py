from pico2d import *
import Logo
import Player1
import Player2 
import home
import fightBack
import Power

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
    global player1, player2
    global randomPower

    player1 = Player1.Player1()
    player2 = Player2.Player2()
    FightBackground = fightBack.Background()
    randomPower = Power.Power()

def update():
    global player1, player2
    player1.update()
    player2.update()

def drawScene():
    clear_canvas()

    FightBackground.draw()

    player1.draw()
    player2.draw()
    if randomPower.draw:
        randomPower.ShowGetPower(1)
        randomPower.ShowGetPower(2)

    update_canvas()

def Process_event(run_game):
    global player1, player2

    events = get_events()

    run_game = player1.ProcessEvent(run_game, events)
    run_game = player2.ProcessEvent(run_game, events)
    
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

        delay(0.01)

#main

draw_Logo()

open_canvas(1200, 800)

mainHome_Init()

draw_home()

if run_game == True : 
    fightSpace_Init()
    print("enter fight map")


while run_game:
    randomPower.endTime = get_time()

    if randomPower.endTime - randomPower.startTime > 30:
        randomPower.GetPower(player1)
        randomPower.GetPower(player2)
        randomPower.startTime = randomPower.endTime
        randomPower.ShowGetPower(1)
        randomPower.ShowGetPower(2)
        print("Get random Power")
        randomPower.draw = True


    
    run_game = Process_event(run_game)

    update()

    drawScene()
    if randomPower.draw:
        delay(2)
        randomPower.draw = False

    delay(0.01)

close_canvas