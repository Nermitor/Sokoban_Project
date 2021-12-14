import pygame as pg

import config
from game import main as game
from help import main as hlp


def check_mouse(pos, rect):
    x, y = pos
    return rect.x <= x <= rect.x + rect.width and rect.y <= y <= rect.y + rect.height


def main():
    pg.init()
    screen = pg.display.set_mode(config.MENU_SIZE)

    font = pg.font.SysFont("Arial", 80)

    f1 = font.render("Начать игру", True, (255,) * 3)
    rect1 = f1.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] / 9))

    f2 = font.render("Инфо", True, (255,) * 3)
    rect2 = f2.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] / 2))

    f3 = font.render("Выход", True, (255,) * 3)
    rect3 = f3.get_rect(center=(config.MENU_SIZE[0] / 2, config.MENU_SIZE[1] / 1.1))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                if check_mouse(pos, rect1):
                    game()
                elif check_mouse(pos, rect2):
                    hlp("help.txt")
                    main()
                elif check_mouse(pos, rect3):
                    running = False

        pg.display.update()
        screen.blit(f1, rect1)
        screen.blit(f2, rect2)
        screen.blit(f3, rect3)


main()
