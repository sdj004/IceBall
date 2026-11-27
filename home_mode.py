import frame_work
import play_mode
from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    SDLK_RETURN,
    clear_canvas,
    get_events,
    load_image,
    update_canvas,
)


class HomeMode:
    def init(self):
        self.image = load_image("mainBackground.png")

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                frame_work.quit()
                return
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    frame_work.quit()
                    return
                if event.key == SDLK_RETURN:
                    frame_work.change_mode(play_mode.PlayMode())
                    return

    def update(self):
        pass

    def render(self):
        clear_canvas()
        self.image.draw(600, 400, 1200, 800)
        update_canvas()

    def finish(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass
