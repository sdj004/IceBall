from pico2d import *

class Intro:
    def __init__(self):
        self.image = load_image("tuk_credit.png")

    def draw(self):
        self.image.draw(600, 400)
