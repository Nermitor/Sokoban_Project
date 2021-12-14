from pygame.image import load
from pygame.transform import scale

from config import CELL_SIZE


def resize(file_name):
    return scale(load(file_name), (CELL_SIZE,) * 2)
