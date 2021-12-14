import pygame as pg

import config
from pysprites.box import Box
from pysprites.dock import Dock
from pysprites.player import Player
from pysprites.wall import Wall


class Map:
    def __init__(self, level_number):
        self.player = None
        self.map = []
        self.size_x, self.size_y = None, None
        self.player_pos = None
        self.player = None
        self.level = level_number
        self.to_win_cords = []
        self.load_level(level_number)

    def draw(self, screen):
        for y, x in self.to_win_cords:
            screen.blit(Dock().image, (x * config.CELL_SIZE, y * config.CELL_SIZE))
        for y in range(self.size_y):
            for x in range(self.size_x):
                if (sprite := self.map[y][x]) is not None:
                    screen.blit(sprite.image, (config.CELL_SIZE * x, config.CELL_SIZE * y))

    def update(self):

        keys = pg.key.get_pressed()
        move = (0, 0)
        if keys[pg.K_w]:
            move = (-1, 0)
        elif keys[pg.K_s]:
            move = (1, 0)
        elif keys[pg.K_a]:
            move = (0, -1)
        elif keys[pg.K_d]:
            move = (0, 1)
        if move != (0, 0):
            if self.check_move(self.player_pos, self.tuple_sum(self.player_pos, move)):
                h = self.player_pos, move
                self.get_move(self.tuple_sum(self.player_pos, move))
        if self.on_win_check():
            return True
        return False

    def load_level(self, n):
        with open(f"levels/{n}.txt") as file:
            self.size_x = int(file.readline().split()[-1])
            self.size_y = int(file.readline().split()[-1])
            self.map = [[None for _ in range(self.size_x)] for __ in range(self.size_y)]
            for y in range(self.size_y):
                row = file.readline()
                for x in range(self.size_x):
                    if row[x] == "X":
                        self.map[y][x] = Wall()
                    elif row[x] == "*":
                        self.map[y][x] = Box()
                    elif row[x] == ".":
                        self.map[y][x] = Dock()
                        self.to_win_cords.append((y, x))
                    elif row[x] == "@":
                        self.map[y][x] = Player()
                        self.player_pos = y, x

    def check_move(self, from_, to_):
        if type(self.get_from_index(to_)) is Wall:
            return False

        if type(self.get_from_index(to_)) is Box:
            if type(self.get_from_index(self.get_2x_to(from_, self.get_dir(from_, to_)))) in (Wall, Box):
                return False
        return True

    def get_move(self, to_):
        if type(self.get_from_index(to_)) is Box:
            self.set_from_index(self.get_2x_to(self.player_pos, self.get_dir(self.player_pos, to_)), Box())
        self.set_from_index(to_, Player())
        self.set_from_index(self.player_pos, None)
        self.player_pos = to_

    def on_win_check(self):
        for y, x in self.to_win_cords:
            if type(self.get_from_index((y, x))) is not Box:
                return False
        return True

    def get_2x_to(self, from_, dir_):
        return self.tuple_sum(from_, self.tuple_mult(dir_, 2))

    def get_from_index(self, cords):
        f = self.map[cords[0]][cords[1]]
        return f

    def set_from_index(self, cords, item):
        self.map[cords[0]][cords[1]] = item

    def get_dir(self, p1, p2):
        return p2[0] - p1[0], p2[1] - p1[1]

    @staticmethod
    def tuple_sum(a, b):
        f = a[0] + b[0], a[1] + b[1]
        return f

    @staticmethod
    def tuple_mult(a, b):
        return a[0] * b, a[1] * b
