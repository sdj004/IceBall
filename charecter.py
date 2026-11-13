from pico2d import *
from transitions import Machine

class Charecter:
    def __init__(self):
        self.run = load_image("run1.png")
        self.hit = load_image("hit1.png")
        self.throw = load_image("throwSnowBall1.png")
        self.x = 200
        self.y = 200
        self.dirX = 0
        self.dirY = 0
        self.frame = 0
        self.action = 0

        self.machine = Machine(
            model=self,
            states=['IDLE', 'HIT', 'RUN', 'THROW', "MAKE"],
            transitions=[
                {'trigger': 'start_throw',
                 'source': ['RUN', 'IDLE', 'MAKE'], 'dest': 'THROW'},
                {'trigger': 'start_hit',
                 'source': ['THROW', 'IDLE', 'MAKE', 'RUN'], 'dest': 'HIT'},
                {'trigger': 'start_run',
                 'source': ['IDLE', 'MAKE', 'RUN', 'THROW'], 'dest': 'RUN'},
                {'trigger': 'stop_run',
                 'source': 'RUN', 'dest': 'IDLE'},
            ],
                initial='IDLE',
                auto_transitions=False,
        )

    def draw(self):
        if self.state in "RUN":
            self.run.clip_draw(self.frame, self.action, 720, 720, self.x, self.y, 300, 300)

    def update(self):
        self.x += self.dirX * 5
        self.y += self.dirY * 5

    def ProcessEvent(self, run_game):
        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                run_game = False
                break

            if self.state in ('IDLE', 'MAKE', 'RUN', 'THROW'):
               
                if event.type == SDL_KEYDOWN and event.key == SDLK_a:
                    self.dirX -= 1
                    self.start_run()
                elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                    self.dirX += 1
                    self.start_run()
                elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
                    self.dirY += 1
                    self.start_run()
                elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
                    self.dirY -= 1
                    self.start_run()
                elif event.type == SDL_KEYUP and event.key == SDLK_a:
                    self.dirX += 1
                    self.start_run()
                elif event.type == SDL_KEYUP and event.key == SDLK_d:
                    self.dirX -= 1
                    self.start_run()
                elif event.type == SDL_KEYUP and event.key == SDLK_w:
                    self.dirY -= 1
                    self.start_run()
                elif event.type == SDL_KEYUP and event.key == SDLK_s:
                    self.dirY += 1
                    self.start_run()

        return run_game
            