from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image("fightBackground.png")

    def draw(self):
        self.image.draw(600, 400, 1200, 800)