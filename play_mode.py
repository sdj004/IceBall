import frame_work
import Player1
import Player2
import Power
import fightBack
import game_world

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    SDLK_KP_MULTIPLY,
    clear_canvas,
    get_events,
    get_time,
    update_canvas,
)


POWER_INTERVAL = 30.0
POWER_DISPLAY_DURATION = 2.0

class PlayMode:
    def init(self):
        self.player1 = Player1.Player1()
        self.player2 = Player2.Player2()
        self.background = fightBack.Background()
        self.power = Power.Power()
        self.power.startTime = get_time()
        self.power_display_until = 0.0
        game_world.add_object(self.background, 0)
        game_world.add_object(self.player1, 1)
        game_world.add_object(self.player2, 1)

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                frame_work.quit()
                return
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                frame_work.quit()
                return
            if event.type == SDL_KEYDOWN and event.key == SDLK_KP_MULTIPLY:
                print("show Collision Box")
                if game_world.check_collision_box == False : game_world.check_collision_box = True
                else : game_world.check_collision_box = False

        running = self.player1.ProcessEvent(True, events, self.player2)
        running = self.player2.ProcessEvent(running, events, self.player1)
        if not running:
            frame_work.quit()

    def update(self):
        # self.player1.update()
        # self.player2.update()
        game_world.update()
        now = get_time()
        if now - self.power.startTime >= POWER_INTERVAL:
            self.power.GetPower(self.player1, 1)
            self.power.GetPower(self.player2, 2)
            self.power.startTime = now
            self.power.shoulddraw = True
            self.power_display_until = now + POWER_DISPLAY_DURATION
        elif self.power.shoulddraw and now >= self.power_display_until:
            self.power.shoulddraw = False

    def render(self):
        clear_canvas()
        # self.background.draw()
        # self.player1.draw()
        # self.player2.draw()
        # if self.power.draw:
        #     self.power.ShowGetPower(1)
        #     self.power.ShowGetPower(2)
        game_world.render()

        if self.power.shoulddraw:
             self.power.draw(1)
             self.power.draw(2)
        update_canvas()

    def finish(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass
