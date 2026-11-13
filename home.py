from pico2d import *

class Home:
    def __init__(self):
        self.image = load_image("mainBackground.png")

    def draw(self):
        self.image.draw(600, 400)

    def ProcessEvent():
        events = get_events()

        for event in events:
            if event == SDL_KEYDOWN and event == SDLK_ESCAPE:
                close_canvas()
            