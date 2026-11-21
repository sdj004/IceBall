import random
from pico2d import *


class Power:
    def __init__(self):
        self.startTime = 0.0
        self.endTime = 0.0
        self.power = None
        self.MakeFast = load_image("MakeFast.png")
        self.SnowBallBigger = load_image("SnowBallBigger.png")
        self.CharecterSpeedUp = load_image("CharecterSpeedUp.png")
        self.CharecterSpeedDown = load_image("CharecterSpeedDown.png")
        self.CharecterBigger = load_image("CharecterBigger.png")
        self.CharecterSmaller = load_image("CharecterSmaller.png")
        self.SnowBallSpeedUp = load_image("SnowBallSpeedUp.png")
        self.SnowBallSpeedDown = load_image("SnowBallSpeedDown.png")
        self.ThrowTwice = load_image("ManySnowBall.png")
        self.Card = load_image("PowerCard.png")
        self.GiftBox = load_image("giftBox.png")
        self.powerSize = 300
        self.CardSize = 500
        self.GiftBoxSize = 200
        self.draw = False

    def GetPower(self, player):
        index = random.randint(0, 8)
        
        self.power = index

        if index == 0:
            player.makeTime = 0.325
        elif index == 1:
            player.Snow.xSize = 200
            player.Snow.ySize = 200
        elif index == 2:
            pass
        elif index == 3:
            pass
        elif index == 4:
            player.xSize = 500
            player.ySize = 500
        elif index == 5:
            player.xSize = 100
            player.ySize = 100
        elif index == 6:
            pass
        elif index == 7:
            pass
        elif index == 8:
            pass

    def ShowGetPower(self, who):
        if who == 1 : self.Card.draw(300, 400, self.CardSize, self.CardSize)
        else : self.Card.draw(900, 400, self.CardSize, self.CardSize)

        if self.power == 0:
            if who == 1: self.MakeFast.draw(300, 400, self.powerSize, self.powerSize)
            else : self.MakeFast.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 1:
            if who == 1: self.SnowBallBigger.draw(300, 400, self.powerSize, self.powerSize)
            else : self.SnowBallBigger.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 2:
            if who == 1: self.CharecterSpeedUp.draw(300, 400, self.powerSize, self.powerSize)
            else : self.CharecterSpeedUp.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 3:
            if who == 1: self.CharecterSpeedDown.draw(300, 400, self.powerSize, self.powerSize)
            else : self.CharecterSpeedDown.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 4:
            if who == 1: self.CharecterBigger.draw(300, 400, self.powerSize, self.powerSize)
            else : self.CharecterBigger.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 5:
            if who == 1: self.CharecterSmaller.draw(300, 400, self.powerSize, self.powerSize)
            else : self.CharecterSmaller.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 6:
            if who == 1: self.SnowBallSpeedUp.draw(300, 400, self.powerSize, self.powerSize)
            else : self.SnowBallSpeedUp.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 7:
            if who == 1: self.SnowBallSpeedDown.draw(300, 400, self.powerSize, self.powerSize)
            else : self.SnowBallSpeedDown.draw(900, 400, self.powerSize, self.powerSize)
        elif self.power == 8:
            if who == 1: self.ThrowTwice.draw(300, 400, self.powerSize, self.powerSize)
            else : self.ThrowTwice.draw(900, 400, self.powerSize, self.powerSize)
       
       