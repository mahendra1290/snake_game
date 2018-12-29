import pygame
class Snake:
    snake_list = []
    move_list  = []
    pos_list   = []
    temp_point = (7,0,3,4)
    #move_diret = [1, 0]
    def __init__(self, size, color, screen):
        self.color = color
        self.head_color = (155, 155, 155)
        self.x = 0 
        self.y = 0
        self.speed = 7
        self.width  = size
        self.height = size
        self.screen = screen
        #self.rect   = ([self.speed, 0], [self.x, self.y, self.width, self.height])
        #self.snake_list = [self.rect]
        #self.head_circle = (self.screen, self.color, [3.5, 3.5], 3.5)
        #self.snake_list.append(self.head_circle)
        for i in range(2):
            temp = ([self.speed, 0], [self.x, self.y ,self.width, self.height],self.color)
            self.snake_list.append(temp)
            self.x -= self.speed
        self.x = 0

    def update_snake(self, color):
        last_x = self.snake_list[-1][1][0]
        last_y = self.snake_list[-1][1][1]
        last_xx = self.snake_list[-2][1][0]
        last_yy = self.snake_list[-2][1][1]
        #print(f"last_x {last_x} and last_y {last_y}")
        #print(f"last_xx {last_xx} and last_yy {last_yy}")
        x = self.snake_list[-1][0][0]
        y = self.snake_list[-1][0][1]
        if last_x == last_xx:
            print("y ", y)
            temp = ([x, y],[last_x, last_y-y, self.width, self.height], color)
            print("x_axis")
        else:
            print("x ", x)
            temp = ([x, y],[last_x-x, last_y, self.height, self.width], color)
            print("y_axis")
        self.snake_list.append(temp)

    def update_pos_list(self):
        temp_dict = {'x':self.x, 'y':self.y}
        self.pos_list.append(temp_dict)

    def get_snake(self):
        """return copy of our move_list"""
        snake_data = self.pos_list.copy()
        head = self.get_pos()
        tail = self.get_pos(head=False)
        snake_data.insert(0, head)
        snake_data.append(tail)
        return snake_data
    
    def snake_move(self):
        """moves snake according to input"""
        lent = len(self.snake_list)-1
        for i in range(len(self.snake_list)):
            for j in self.move_list:
                #print(f"snake[{i}][1][0] = {self.snake_list[i][1][0]}")
                if self.snake_list[i][1][0] == j[2] and self.snake_list[i][1][1] == j[3]:
                    self.snake_list[i][0][0] = j[0]
                    self.snake_list[i][0][1] = j[1]
                    if(i==lent):
                        self.move_list.remove(self.move_list[0])
                        self.pos_list.remove(self.pos_list[0])
                    break
        
        for i in range(len(self.snake_list)):
            self.snake_list[i][1][0] += self.snake_list[i][0][0]
            self.snake_list[i][1][1] += self.snake_list[i][0][1]
            if(not i):
                pygame.draw.rect(self.screen, self.head_color, self.snake_list[i][1])
            else:
                pygame.draw.rect(self.screen, self.snake_list[i][2], self.snake_list[i][1])
        self.x += self.snake_list[0][0][0]
        self.y += self.snake_list[0][0][1]

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
        if(self.temp_point[0] != self.speed and self.temp_point[0] != -self.speed):
            self.temp_point = (-self.speed, 0, self.x, self.y)
            self.move_list.append(self.temp_point)
            self.update_pos_list()

    def move_right(self):
        """to change direction to right"""
        if(self.temp_point[0] != self.speed and self.temp_point[0] != -self.speed):
            self.temp_point = (self.speed, 0, self.x, self.y)
            self.move_list.append(self.temp_point)
            self.update_pos_list()

    def move_up(self):
        """to change direction to up"""
        if(self.temp_point[1] != self.speed and self.temp_point[1] != -self.speed):
            self.temp_point = (0, -self.speed, self.x, self.y)
            self.move_list.append(self.temp_point)
            self.update_pos_list()

    def move_down(self):
        """to change direction to down"""
        if(self.temp_point[1] != self.speed and self.temp_point[1] != -self.speed):
            self.temp_point = (0, self.speed, self.x, self.y)
            self.move_list.append(self.temp_point)
            self.update_pos_list()


    




