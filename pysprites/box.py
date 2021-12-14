import pygame as pg

from image import resize


class Box(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = resize("sprites/box.png")
        self.image.set_colorkey((254, 220, 178))
        self.rect = self.image.get_rect()
