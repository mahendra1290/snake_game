import pygame
class Font:
    def __init__(self, font, size):
        self.font = font
        self.size = size
        self.font_obj = pygame.font.Font(font, size)

