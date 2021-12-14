import pygame as pg

from image import resize


class Wall(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = resize("sprites/wall.png")
        self.rect = self.image.get_rect()
