import pygame
class Snake:
    snake_list = []
    snake_part = []
    head_direct  = {'x':0, 'y':0, 'dir':'e', 'chng':'-'}
    head_cord    = {'x':0, 'y':0, 'dir':'e', 'chng':'-'}
    snake_lenth  = 0
    change = False
    def __init__(self, screen, screen_size, speed, snake):
        self.head = snake['head']
        self.tail = snake['tail']
        self.body = snake['body']
        self.speed = speed
        self.screen = screen
        self.screen_size = screen_size
        self.head_direct['x'] = self.speed
        self.snake_part.append(self.head)
        self.snake_list.append(self.head_cord)
        self.snake_lenth += 1

        for i in range(1, 2):
            temp = {'x':-self.speed*i, 'y':0, 'dir':'e', 'chng':'-'}
            self.snake_list.append(temp)
            self.snake_part.append(self.body)
            self.snake_lenth += 1

        temp = {'x':-self.speed*2, 'y':0, 'dir':'e', 'chng':'-'}
        self.snake_list.append(temp)
        self.snake_part.append(self.tail)
        self.snake_lenth += 1
        
    def snake_move(self):
        self.head_cord['x']  += self.head_direct['x']
        self.head_cord['y']  += self.head_direct['y']
        self.head_cord['dir'] = self.head_direct['dir']
        self.head_cord['chng'] = self.head_direct['chng']
        temp = self.head_cord.copy()
        self.snake_list.append(temp)
        if self.change:
            self.snake_list[-2]['dir'] = self.head_direct['dir']
            self.snake_list[-2]['chng'] = self.head_direct['chng']
        self.head_direct['chng'] = '-'
        if len(self.snake_list) > self.snake_lenth:
            self.snake_list.remove(self.snake_list[0])
        #print(self.snake_list)
        z = -1
        for i, j in zip(self.snake_list, self.snake_part):
            if (i['chng'] != '-') and (self.snake_part.index(j) != 0 and self.snake_part.index(j) != (len(self.snake_part)-1)):
                self.screen.blit(self.snake_part[z][i['chng']], (i['x'], i['y']))

            elif self.snake_part.index(j) == 0:
                offset = {'w':[0, 0], 'e':[-5, 0], 'n':[0, 0], 's':[0, -5]}
                temp_direc = i['dir']
                self.screen.blit(self.snake_part[z][i['dir']], (i['x']+offset[temp_direc][0], i['y']+offset[temp_direc][1]))

            elif self.snake_part.index(j) == (len(self.snake_part)-1):
                offset = {'w':[-5, 0], 'e':[0, 0], 'n':[0, -5], 's':[0, 0]}
                temp_direc = i['dir']
                self.screen.blit(self.snake_part[z][i['dir']], (i['x']+offset[temp_direc][0], i['y']+offset[temp_direc][1]))

            else:
                self.screen.blit(self.snake_part[z][i['dir']], (i['x'], i['y']))
                
            if self.change:
                self.snake_list[-1]['chng'] = '-'
                self.change = False
            z -= 1

    def update_snake(self):
        scnd_last = self.snake_list[1]
        self.snake_list.insert(1, scnd_last)
        self.snake_part.insert(1, self.body)

    def get_snake(self):
        snake_cordinate = []
        for i in self.snake_list:
            cord = {'x':i['x'], 'y':i['y']}
            snake_cordinate.append(cord)
        return snake_cordinate

    def self_collision(self):
        """returns true if collision happens with itself"""
        for v, i in enumerate(self.snake_list):
            if v == len(self.snake_list)-1:
                continue
            if i['x'] == self.head_cord['x'] and i['y'] == self.head_cord['y']:
                return True
        return False

    def is_collision(self, x, y):
        """if snake head is collided with point at x, y"""
        if x == self.head_cord['x'] and y == self.head_cord['y']:
            return True
        return False

    def turn_left_right(self, right=True):
        """move right by default"""
        if self.head_direct['x'] is 0:
            t_dir = self.head_direct['dir']
            if right:
                self.head_direct['x'] = self.speed
                self.head_direct['dir'] = 'e'
            else:
                self.head_direct['x'] = -self.speed
                self.head_direct['dir'] = 'w'
            self.head_direct['chng'] = t_dir+self.head_direct['dir'] 
            self.head_direct['y'] = 0
            self.change = True

    def turn_up_down(self, down=True):
        """move down by default"""
        if self.head_direct['y'] is 0:
            t_dir = self.head_direct['dir']
            if down:
                self.head_direct['y'] = self.speed   
                self.head_direct['dir'] = 's'
            else:
                self.head_direct['y'] = -self.speed
                self.head_direct['dir'] = 'n'
            self.head_direct['chng'] = t_dir+self.head_direct['dir']
            self.head_direct['x'] = 0
            self.change = True



