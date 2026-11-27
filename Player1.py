from pico2d import *
from transitions import Machine
import frame_work
import math
import game_world
import pico2d.pico2d as pico2d_core

mouseclick = 0
class Snow:
    def __init__(self, x, y):
        self.x = x + 50.0
        self.y = y + 20.0
        self.xSize = 100
        self.ySize = 100
        self.exist = False
        self.SnowBall = load_image("SnowBall.png")

    def draw(self):
        if self.exist : self.SnowBall.draw(self.x, self.y, self.xSize, self.ySize)
        if self.exist and game_world.check_collision_box : draw_rectangle(*self.get_bb())

    def update(self, Mx, My, playerX, playerY):
        moveX = abs(Mx - playerX) / 30
        moveY = (800 - My - playerY) / 30
        
        self.x += moveX
        self.y += moveY

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def handle_collision(self, group, other):
        if group == "player2:snowball" : 
            print("hit")
            self.exist = False

class Player1:
    def __init__(self):
        self.run = load_image("run1.png")
        self.hit = load_image("hit1.png")
        self.throw = load_image("throwSnowBall1.png")
        self.make = load_image("makeSnowBall1.png")
        self.x = 200.0
        self.y = 200.0
        self.dirX = 0
        self.dirY = 0
        self.DirX = 'right'
        self.DirY = 'up'
        self.frame = 0
        self.action = 0
        self.snowBall = False
        self.startMake = 0
        self.endMake = 0
        self.Mx = 0.0
        self.My = 0.0
        self.xSize = 300.0
        self.ySize = 300.0
        self.makeTime = 0.75
        self.Snow = Snow(self.x, self.y)
        self.PIXEL_PER_METER = (300.0 / 1.7)
        self.RUN_SPEED_KMPH = 10.0
        self.RUN_SPEED_MPM = (self.RUN_SPEED_KMPH * 1000.0 / 60.0)
        self.RUN_SPEED_MPS = (self.RUN_SPEED_MPM / 60.0)
        self.RUN_SPEED_PPS = (self.RUN_SPEED_MPS * self.PIXEL_PER_METER)
        self.STRIDE_LENGTH_M = 0.8
        self.RUN_FRAMES_PER_STRIDE = 12
        self.RUN_FRAMES_PER_SECOND = self.RUN_SPEED_MPS / self.STRIDE_LENGTH_M * self.RUN_FRAMES_PER_STRIDE
        self.run_frame_progress = 0.0

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
            if self.DirX == "right" : self.run.clip_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))
            else : self.run.clip_composite_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, 0, 'h', self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))

        if self.state in "IDLE":
            if self.DirX == "right" : self.make.clip_draw(0 * 720, 6 * 720, 720, 720, self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))
            else : self.make.clip_composite_draw(0 * 720, 6 * 720, 720, 720, 0, 'h', self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))

        if self.state in "MAKE":
            if self.DirX == "right" : self.make.clip_draw(self.frame * 720, (6 - self.action) * 720, 720, 720, self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))
            else : self.make.clip_composite_draw(self.frame * 720, (6 - self.action) * 720, 720, 720, 0, 'h', self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))

        if self.state in "THROW":
            self.throw.clip_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, self.x, self.y, self.ySize - (self.y * 0.2), self.ySize - (self.y * 0.2))
            self.Snow.draw()

        if self.state in "HIT":
            pico2d_core.SDL_SetRenderDrawBlendMode(
                pico2d_core.renderer,
                pico2d_core.SDL_BLENDMODE_BLEND,
            )
            draw_circle(self.x, self.y, 150, 255, 0, 0, 127, True)
            if self.DirX == "right" : self.hit.clip_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, self.x, self.y, self.ySize - (self.y * 0.2), self.ySize - (self.y * 0.2))
            else : self.hit.clip_composite_draw(self.frame * 720, (5 - self.action) * 720, 720, 720, 0, 'h', self.x, self.y, self.xSize - (self.y * 0.2), self.ySize - (self.y * 0.2))

    def update(self):
        if self.state in "HIT":
            if self.action == 5: 
                self.frame = (self.frame + 1) % 3
                if self.frame == 2 :
                    self.action = 0
                    self.frame = 0
                    self.start_idle()
            else : 
                self.frame = (self.frame + 1) % 12
                if self.frame == 11:
                    self.action = (self.action + 1) % 6
                    self.frame = 0

        if self.state in "RUN":
            frame_count = self.RUN_FRAMES_PER_STRIDE
            frames_per_second = self.RUN_FRAMES_PER_SECOND
            self.run_frame_progress = (
                self.run_frame_progress
                + frames_per_second * frame_work.frame_time
            ) % frame_count
            self.frame = int(self.run_frame_progress)

        if self.state in "MAKE":
            self.frame = (self.frame + 1) % 12
            if self.frame == 11 : 
                self.action = (self.action + 1) % 7
                self.frame = 0

        if self.state in "THROW":
            self.Snow.update(self.Mx, self.My, self.x, self.y)

            if self.action < 5 : 
                self.frame = (self.frame + 1) % 12
                if self.frame == 11: 
                    self.action = (self.action + 1) % 6
                    self.frame = 0
            else : 
                self.frame = (self.frame + 1) % 3
                if self.frame == 2 : 
                    self.action = 0
                    self.frame = 0
                    self.start_idle()

            game_world.handle_collisions()

        direction_length = math.hypot(self.dirX, self.dirY)
        direction_x = self.dirX
        direction_y = self.dirY
        if direction_length > 1.0:
            direction_x /= direction_length
            direction_y /= direction_length

        frame_time = frame_work.frame_time
        next_x = self.x + direction_x * self.RUN_SPEED_PPS * frame_time
        next_y = self.y + direction_y * self.RUN_SPEED_PPS * frame_time
        if 100.0 < next_x < 500.0:
            self.x = next_x
        if 200.0 < next_y < 400.0:
            self.y = next_y

    def ProcessEvent(self, run_game, events, player2):
        global mouseclick
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
                        self.Snow.exist = True
                        print(f"{mouseclick} : mouse click")
                        mouseclick += 1
                        game_world.add_collision_pair("player2:snowball", player2, self.Snow)
                        

            if self.state in ('IDLE', 'MAKE'):
                if (
                    self.state == "IDLE"
                    and event.type == SDL_KEYDOWN
                    and event.key == SDLK_LSHIFT
                ):
                    self.startMake = get_time()
                    self.make_snowball()
                elif (
                    self.state == "MAKE"
                    and event.type == SDL_KEYUP
                    and event.key == SDLK_LSHIFT
                ):
                    self.endMake = get_time()
                    print(f"make time : {self.endMake - self.startMake}")
                    MakeTime = self.endMake - self.startMake
                    if MakeTime >= self.makeTime: 
                        self.snowBall = True
                        self.Snow.x = self.x + 50
                        self.Snow.y = self.y + 20
                    self.start_idle()
                    self.frame = 0
                    self.action = 0
                    self.run_frame_progress = 0.0

            if self.state in ('IDLE', 'MAKE', 'RUN', 'THROW'):
                if event.type == SDL_KEYDOWN and event.key == SDLK_a:
                    self.action = 0
                    if self.DirX == "right" : self.dirX = 0.0
                    self.dirX -= 1.0
                    self.start_run()
                    self.DirX = "left"
                    print("left")
                if event.type == SDL_KEYDOWN and event.key == SDLK_d:
                    self.action = 0
                    if self.DirX == "left" : self.dirX = 0.0
                    self.dirX += 1.0
                    self.start_run()
                    self.DirX = "right"
                    print("right")
                if event.type == SDL_KEYDOWN and event.key == SDLK_w:
                    self.action = 0
                    if self.DirY == "down" : self.dirY = 0.0
                    self.dirY += 1.0
                    self.start_run()
                    self.DirY = "up"
                    print("up")
                if event.type == SDL_KEYDOWN and event.key == SDLK_s:
                    self.action = 0
                    if self.DirY == "up" : self.dirY = 0.0
                    self.dirY -= 1.0
                    self.start_run()
                    self.DirY = "down"
                    print("down")
                elif (
                    self.state in "RUN"
                    and event.type == SDL_KEYUP
                    and event.key in (SDLK_a, SDLK_d, SDLK_w, SDLK_s)
                ):
                    self.start_idle()
                    if self.dirX < 0 : self.dirX += 1.0
                    elif self.dirX > 0 : self.dirX -= 1.0

                    if self.dirY < 0 : self.dirY += 1.0
                    elif self.dirY > 0 : self.dirY -= 1.0

                    self.frame = 0
                    self.action = 0
                    self.run_frame_progress = 0.0
                    print("None")

        return run_game

    def get_bb(self):
        if self.state in "RUN":
            bounds = (-60, -100, 60, 100)
        elif self.state in "IDLE":
            bounds = (-25, -110, 25, 110)
        elif self.state in "MAKE" and 2 <= self.action <= 4:
            bounds = (-50, -115, 50, 70)
        elif self.state in "MAKE":
            bounds = (-50, -110, 50, 100)
        elif self.state in "THROW":
            bounds = (-40, -110, 40, 110)
        elif self.state in "HIT":
            bounds = (-60, -100, 60, 100)
        else:
            return None

        if self.xSize > 300.0:
            scale_x = 1.0 + (self.xSize - 300.0) / 300.0
        elif self.xSize < 300.0:
            scale_x = 1.0 - (300.0 - self.xSize) / 300.0
        else:
            scale_x = 1.0

        if self.ySize > 300.0:
            scale_y = 1.0 + (self.ySize - 300.0) / 300.0
        elif self.ySize < 300.0:
            scale_y = 1.0 - (300.0 - self.ySize) / 300.0
        else:
            scale_y = 1.0

        left, bottom, right, top = bounds
        return (
            self.x + left * scale_x,
            self.y + bottom * scale_y,
            self.x + right * scale_x,
            self.y + top * scale_y,
        )

    def handle_collision(self, group, other):
        global game_framework
        
        if group == "player1:snowball":
            print("player 1: out")
            if self.state != "HIT" : 
                self.start_hit()
                self.action = 0
                self.frame = 0
       