import pygame
class Snake:
    snake_list = []
    head_direct  = {'x':0, 'y':0}
    head_cord    = {'x':0, 'y':0}
    snake_lenth  = 0
    def __init__(self, size, color, screen, screen_size, speed):
        self.color = color
        self.head_color = (155, 155, 155)
        self.x = 0
        self.y = 0
        self.speed = speed
        self.size  = size
        self.screen = screen
        self.screen_size = screen_size
        self.head_direct['x'] = self.speed
        temp = {'x':0, 'y':0, 'color':self.color}
        self.snake_list.append(self.head_cord)
        self.snake_lenth += 1
        temp = {'x':-self.speed, 'y':0, 'color':self.color}
        self.snake_list.append(temp)
        self.snake_lenth += 1
        
    def snake_move(self):
        self.head_cord['x'] += self.head_direct['x']
        self.head_cord['y'] += self.head_direct['y']
        temp = self.head_cord.copy()
        self.snake_list.append(temp)
        if len(self.snake_list) > self.snake_lenth:
            self.snake_list.remove(self.snake_list[0])
        for i in self.snake_list:
            pygame.draw.rect(self.screen, self.color,[i['x'], i['y'], self.size, self.size])

    def update_snake(self, color):
        pass

    def get_snake(self):
        """return copy of our move_list"""
        pass

    def get_pos(self, head=True):
        """returns position if head==True and tail if head==False"""
        if head:
            return {'x':self.x, 'y':self.y}
        else:
            end_x = self.snake_list[-1][1][0]
            end_y = self.snake_list[-1][1][1]
            return {'x':end_x, 'y':end_y}

    def move_left(self):
        """to change direction to left"""
        if (self.head_direct['x'] is not self.speed) and (self.head_direct['x'] is not -self.speed):
            self.head_direct['x'] = -self.speed
            self.head_direct['y'] = 0

    def move_right(self):
        """to change direction to right"""
        if (self.head_direct['x'] is not self.speed) and (self.head_direct['x'] is not -self.speed):
            self.head_direct['x'] = self.speed
            self.head_direct['y'] = 0

    def move_up(self):
        """to change direction to up"""
        if (self.head_direct['y'] is not self.speed) and (self.head_direct['y'] is not -self.speed):
            self.head_direct['y'] = -self.speed
            self.head_direct['x'] = 0

    def move_down(self):
        """to change direction to down"""
        if (self.head_direct['y'] is not self.speed) and (self.head_direct['y'] is not -self.speed):
            self.head_direct['y'] = self.speed
            self.head_direct['x'] = 0



