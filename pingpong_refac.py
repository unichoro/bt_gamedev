import pygame
import math
import random

class game(self):
    def __init__(self):
        pygame.init()
        pygame.font.init()

        window_width = 640
        window_height = 360

        space_color = (16, 72, 98)
        ball_color = (248, 182, 43)
        player_color = (198, 224, 120)

        window = pygame.display.set_mode((window_width, window_height))
        running = True
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000
        font_size = 36
        font = pygame.font.Font("./Arial.ttf", font_size)
