import pickle

import pygame as pg

import config
from map import Map


def set_screen(mp):
    return pg.display.set_mode((mp.size_x * config.CELL_SIZE, mp.size_y * config.CELL_SIZE))


def main(save_existing):
    cur_level = 1
    if save_existing:
        with open("map.pickle", 'rb') as file:
            cur_level = pickle.load(file)
    cur_map = Map(cur_level)
    screen = set_screen(cur_map)
    pg.display.set_caption("Think to get out")
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                with open("map.pickle", "wb") as file:
                    pickle.dump(cur_level, file)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    cur_map = Map(cur_level)
                win = cur_map.update()
                if win:
                    cur_map = Map(cur_level := cur_level + 1)
                    set_screen(cur_map)


        screen.fill("black")
        cur_map.draw(screen)
        pg.display.update()

    pg.quit()
