import pygame as pg

import config


def blit_menu(screen: pg.Surface, text: str, font: pg.font.Font):
    row_num = 0
    for row in text.split('\n'):
        txt = font.render(row, False, (255,) * 3)
        screen.blit(txt, (0, row_num * font.get_height()))
        row_num += 1


def main(file_name):
    pg.init()
    screen = pg.display.set_mode(config.MENU_SIZE)
    pg.display.set_caption("Help")
    help_font = pg.font.SysFont("Arial", 30)  # Шрифт меню
    with open(file_name, encoding='utf-8') as file:
        text = ''.join(file)
    blit_menu(screen, text, help_font)
    pg.display.update()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
