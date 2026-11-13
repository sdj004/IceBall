from pico2d import *
import Logo
import charecter 

def Init():
    global run_game
    global player
    global schoolLogo
    
    run_game = True
    player = charecter.Charecter()
    schoolLogo = Logo.Logo()




def update():
    pass

def draw():
    pass

def Process_event():
    pass

def draw_Logo():
    open_canvas(400, 250)
    clear_canvas()
    Init();
    schoolLogo.draw()
    update_canvas()
    delay(2)
    close_canvas()


def draw_main():
    pass

#main

draw_Logo()

open_canvas(1200, 800)

draw_main()

while run_game:
    clear_canvas()

    Process_event()

    update()

    draw()

    update_canvas()

    delay(0.1)

close_canvas