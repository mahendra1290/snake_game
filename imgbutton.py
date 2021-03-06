import pygame, os

class Button:

    def __init__(self, of_img, on_img, main_path, screen):
        """on_img is displayed on mouse hover and of_img by default"""
        self.on_img = pygame.image.load(os.path.join(main_path, on_img)).convert_alpha()
        self.of_img = pygame.image.load(os.path.join(main_path, of_img)).convert_alpha()
        self.screen = screen
        self.rect_on = self.on_img.get_rect()
        self.rect_of = self.of_img.get_rect()
    
    def set_cor(self, x, y):
        self.rect_on.center = (x, y)
        self.rect_of.center = (x, y)

    def create(self, z, y):
        """render button on screen at x, y coordinate and z is mouse coordinate"""
        #print(self.rect_of.width, self.rect_of.height)
        if self.rect_of.collidepoint(z):
            self.screen.blit(self.on_img, self.rect_on)
        else:
            self.screen.blit(self.of_img, self.rect_of)
        if self.rect_on.collidepoint(z) and y[0] == 1:
            return True
        return False