__author__ = "Gianni"

# pygame
import pygame
from pygame.locals import *

def render_map(window, map):
    x = 0
    y = 0

    for tile_y in map:
        for tile_x in tile_y:
            if tile_x == "1":
                pygame.draw.rect(window, (255,255,255), (x, y, 32, 32), 0)
            elif tile_x == "0":
                pygame.draw.rect(window, (0, 0, 0), (x, y, 32, 32), 0)
            x += 32
        x = 0
        y += 32
    pygame.display.flip()