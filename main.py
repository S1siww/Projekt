import pygame
import random
import time

pygame.init()

width, heigh = 600, 6
velkost_pola = 4
velkost_karty = width // velkost_pola
font = pygame.font.Font(None, 72)
maly_font = pygame.font.Font(None, 36)

biela = (255, 255, 255)
cierna = (0, 0, 0)
siva = (200, 200, 200)
modra = (0, 0, 255)
cervena = (255, 0, 0)