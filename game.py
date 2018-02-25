__author__ = "Gianni"

# pygame
import pygame
from pygame.locals import *

# personal module
import mapfromfile
import rendermap

pygame.init()

window = pygame.display.set_mode((500, 500))
window.fill((195,195,195))

map = mapfromfile.get_map_from_csv_file("testmap.csv")

rendermap.render_map(window, map)

pygame.display.flip()

continuer = 1

while continuer:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0