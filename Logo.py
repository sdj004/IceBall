from pico2d import *

class Logo:
    def __init__(self):
        self.image = load_image("tuk_credit.png")

    def draw(self):
        self.image.draw(200, 125, 800, 600)
