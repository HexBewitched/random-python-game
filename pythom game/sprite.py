import pygame

class Sprite:
    def __init__(self, sprite, x, y, window):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.draw(window)

    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))

    def physics(self, window):
        pass

    def update(self, window):
        self.draw(window)
        self.physics(window)
 
class Player(Sprite):
    def __init__(self, sprite, x, y, window):
        super().__init__(sprite, x, y, window)