from pico2d import *
from transitions import Machine

class Charecter:
    def __init__(self):
        self.run = load_image("run1.png")
        self.hit = load_image("hit1.png")
        self.throw = load_image("throwSnowBall1.png")
        self.make = load_image("makeSnowBall1.png")
        self.x = 200
        self.y = 200
        self.dirX = 0
        self.dirY = 0
        self.DirX = 'right'
        self.DirY = 'up'
        self.frame = 0
        self.action = 0
        self.snowBall = False
        self.startMake = 0
        self.endMake = 0
        self.Mx = 0
        self.My = 0

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
                {'trigger': 'start_idle',
                 'source': ['HIT', 'RUN', 'THROW', "MAKE"], 'dest': 'IDLE'},
                {'trigger' : 'make_snowball',
                 'source' : ['IDLE', 'MAKE'], 'dest' : 'MAKE'}, 
            ],
                initial='IDLE',
                auto_transitions=False,
        )

    def draw(self):
        if self.state in "RUN":
            if self.DirX == "right" : self.run.clip_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))
            else : self.run.clip_composite_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, 0, 'h', self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))

        if self.state in "IDLE":
            if self.DirX == "right" : self.make.clip_draw(0 * 720, 6 * 720, 720, 720, self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))
            else : self.make.clip_composite_draw(0 * 720, 6 * 720, 720, 720, 0, 'h', self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))

        if self.state in "MAKE":
            if self.DirX == "right" : self.make.clip_draw(self.frame * 720, (6 - self.action) * 720, 720, 720, self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))
            else : self.make.clip_composite_draw(self.frame * 720, (6 - self.action) * 720, 720, 720, 0, 'h', self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))

        if self.state in "THROW":
            self.throw.clip_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, self.x, self.y, 300 - (self.y * 0.2), 300 - (self.y * 0.2))

    def update(self):
        if self.state in "RUN":
            if self.action < 5 : 
                self.frame = (self.frame + 1) % 12
                if self.frame == 11: 
                    #self.action = (self.action + 1) % 5
                    self.frame = 0
            else : 
                self.frame = (self.frame + 1) % 3
                if self.frame == 2 : 
                    #self.action = (self.action + 1) % 5
                    self.frame = 0

        if self.state in "MAKE":
            self.frame = (self.frame + 1) % 12
            if self.frame == 11 : 
                self.action = (self.action + 1) % 7
                self.frame = 0

        if self.state in "THROW":
            if self.action < 5 : 
                self.frame = (self.frame + 1) % 12
                if self.frame == 11: 
                    self.action = (self.action + 1) % 6
                    self.frame = 0
            else : 
                self.frame = (self.frame + 1) % 3
                if self.frame == 2 : 
                    self.action = (self.action + 1) % 6
                    self.frame = 0
                    self.start_idle()

        if self.x + self.dirX > 200 and self.x + self.dirX < 500 :  self.x += self.dirX * 5
        if self.y + self.dirY > 200 and self.y + self.dirY < 400 : self.y += self.dirY * 5

    def ProcessEvent(self, run_game):
        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                run_game = False
                break

            if self.state in ('RUN', 'IDLE', 'MAKE'):
                if event.type == SDL_MOUSEBUTTONDOWN:
                    if self.snowBall == True :
                        self.Mx = event.x
                        self.My = event.y
                        self.start_throw()

            if self.state in ('IDLE', 'MAKE'):
                if event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
                    self.startMake = get_time()
                    self.make_snowball()
                elif self.state == "MAKE" and event.type == SDL_KEYUP:
                    self.endMake = get_time()
                    print(f"make time : {self.endMake - self.startMake}")
                    MakeTime = self.endMake - self.startMake
                    if MakeTime >= 0.87: self.snowBall = True
                    self.start_idle()
                    self.frame = 0
                    self.action = 0

            if self.state in ('IDLE', 'MAKE', 'RUN', 'THROW'):
                
                if event.type == SDL_KEYDOWN and event.key == SDLK_a:
                    if self.DirX == "right" : self.dirX = 0
                    self.dirX -= 1
                    self.start_run()
                    self.DirX = "left"
                if event.type == SDL_KEYDOWN and event.key == SDLK_d:
                    if self.DirX == "left" : self.dirX = 0
                    self.dirX += 1
                    self.start_run()
                    self.DirX = "right"
                if event.type == SDL_KEYDOWN and event.key == SDLK_w:
                    if self.DirY == "down" : self.dirY = 0
                    self.dirY += 1
                    self.start_run()
                    self.DirY = "up"
                if event.type == SDL_KEYDOWN and event.key == SDLK_s:
                    if self.DirY == "up" : self.dirY = 0
                    self.dirY -= 1
                    self.start_run()
                    self.DirY = "down"
                elif self.state in "RUN" and event.type == SDL_KEYUP:
                    self.start_idle()
                    if self.dirX < 0 : self.dirX += 1
                    elif self.dirX > 0 : self.dirX -= 1

                    if self.dirY < 0 : self.dirY += 1
                    elif self.dirY > 0 : self.dirY -= 1 

                    self.frame = 0
                    self.action = 0

        return run_game
            