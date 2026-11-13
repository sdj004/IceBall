from pico2d import *

def Init():
    global run_game

    run_game = True


def update():
    pass

def draw():
    pass

def Process_event():
    pass

open_canvas()

Init();

while run_game:
    clear_canvas()

    Process_event()

    update()

    draw()

    update_canvas()

    delay(0.1)

close_canvas