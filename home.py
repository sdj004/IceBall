from pico2d import *

class Home:
    def __init__(self):
        self.image = load_image("mainBackground.png")

    def draw(self):
        self.image.draw(600, 400, 1200, 800)

    def ProcessEvent(self, run_game):
        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                close_canvas()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                close_canvas()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
                print("enter")
                run_game = True


        return run_game
            