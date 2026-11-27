import frame_work
import home_mode
from pico2d import (
    SDL_QUIT,
    clear_canvas,
    get_events,
    get_time,
    load_image,
    update_canvas,
)


LOGO_DURATION = 2.0


class LogoMode:
    def init(self):
        self.image = load_image("tuk_credit.png")
        self.started_at = get_time()

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                frame_work.quit()
                return

    def update(self):
        if get_time() - self.started_at >= LOGO_DURATION:
            frame_work.change_mode(home_mode.HomeMode())

    def render(self):
        clear_canvas()
        self.image.draw(600, 400, 800, 600)
        update_canvas()

    def finish(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass
