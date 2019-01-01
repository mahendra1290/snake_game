import pygame
pygame.init()

class Font:

    def __init__(self, font, size, surface):
        """font style , font size, font surface"""
        self.font = font
        self.size = size
        self.surface = surface
        self.font_obj = pygame.font.Font(font, size)

    def update_font_size(self, font=False, size=False):
        """update font style and size"""
        if font is not False:
            self.font = font
        if size is not False:
            self.size = size
        self.font_obj = pygame.font.Font(self.font, self.size)
    
class Text(Font):
    
    def draw(self, text, color, cord):
        """draws text of color at cord"""
        self.txt_obj = self.font_obj.render(text, True, color)
        self.rect = self.txt_obj.get_rect()
        self.rect.x = cord[0]
        self.rect.y = cord[1]
        self.surface.blit(self.txt_obj, self.rect)

class Flash_text(Font):
    
    def draw(self, text, color, m_color, cord):
        """draws text of color at cord"""
        self.txt_obj = self.font_obj.render(text, True, color)
        self.rect = self.txt_obj.get_rect()
        self.rect.x = cord[0]
        self.rect.y = cord[1]
        z = pygame.mouse.get_pos()
        if self.rect.collidepoint(z):
            self.txt_obj = self.font_obj.render(text, True, m_color)
        self.surface.blit(self.txt_obj, self.rect)
        if self.rect.collidepoint(z):
            if pygame.mouse.get_pressed()[0] == 1:
                print('yesss')
                return True
            else:
                return False

        



        
