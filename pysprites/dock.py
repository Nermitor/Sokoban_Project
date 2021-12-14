import pygame as pg

from image import resize


class Dock(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = resize("sprites/dock.png")
        self.rect = self.image.get_rect()
