import pygame

class Food:
    def __init__(self, size, screen_size):
        """initializing our food"""
        self.x = 0
        self.y = 0
        self.width = size
        self.height = size

    def get_pos(self):
        return (self.x ,self.y)

    def update_food(self, color ,surface, x, y):
        """update snakes food at x, y"""
        self.x = x
        self.y = y
        pygame.draw.rect(surface, color, [self.x, self.y, self.width, self.height])