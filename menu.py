import pygame as pg
import os.path as path

import config
from game import main as game
from help import main as hlp


def check_mouse(pos, rect):
    x, y = pos
    return rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height


def main():
    pg.init()
    screen = pg.display.set_mode(config.MENU_SIZE)
    pg.display.set_caption("Menu")

    font = pg.font.SysFont("Arial", 80)
    save_existing = path.exists("map.pickle")

    f1 = font.render("Новая игра", True, (255,) * 3)
    rect1 = f1.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] * 0.1))

    f2 = font.render("Продолжить", True, (255,) * 3 if save_existing else (150,) * 3)
    rect2 = f2.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] * 0.4))

    f3 = font.render("Инфо", True, (255,) * 3)
    rect3 = f3.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] * 0.7))

    f4 = font.render("Выход", True, (255,) * 3)
    rect4 = f4.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] * 0.9))

    running = True
    while running:

        pg.display.update()
        screen.blit(f1, rect1)
        screen.blit(f3, rect3)
        screen.blit(f4, rect4)
        screen.blit(f2, rect2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                if check_mouse(pos, rect3):
                    hlp("help.txt")
                    main()
                if check_mouse(pos, rect4):
                    pg.quit()
                if check_mouse(pos, rect2) and save_existing or check_mouse(pos, rect1):
                    game(save_existing)


