import pygame, os, time, random, snake, food

pygame.init()
width  = 600
height = 600
feed_color = "asd"
food_infom = 0
tempss = 0
game_cont = False
colors = {
    'blue'   : (0, 0, 255),
    'red'    : (255, 0, 0),
    'green'  : (0,255, 0),
    'orange' : (255, 255, 0),
    'purple' : (0, 255, 255),
    'pink'   : (255, 0, 255),
    'white'  : (255, 255, 255),
    'cyan'   : (156, 222, 254)
}
win    = pygame.display.set_mode((width, height))
head = {'w':pygame.image.load(os.path.join('snake_head', 'head_W.png')).convert_alpha(),
        'e':pygame.image.load(os.path.join('snake_head', 'head_E.png')).convert_alpha(),
        'n':pygame.image.load(os.path.join('snake_head', 'head_N.png')).convert_alpha(),
        's':pygame.image.load(os.path.join('snake_head', 'head_S.png')).convert_alpha()
        }

tail = {'w':pygame.image.load(os.path.join('snake_tail', 'tail_W.png')).convert_alpha(),
        'e':pygame.image.load(os.path.join('snake_tail', 'tail_E.png')).convert_alpha(),
        'n':pygame.image.load(os.path.join('snake_tail', 'tail_N.png')).convert_alpha(),
        's':pygame.image.load(os.path.join('snake_tail', 'tail_S.png')).convert_alpha()
        }

body = {'e':pygame.image.load(os.path.join('snake_body', 'body_X.png')).convert_alpha(),
        'w':pygame.image.load(os.path.join('snake_body', 'body_X.png')).convert_alpha(),
        'n':pygame.image.load(os.path.join('snake_body', 'body_Y.png')).convert_alpha(),
        's':pygame.image.load(os.path.join('snake_body', 'body_Y.png')).convert_alpha(),
        'en':pygame.image.load(os.path.join('snake_body', 'body_EN.png')).convert_alpha(),
        'es':pygame.image.load(os.path.join('snake_body', 'body_ES.png')).convert_alpha(),
        'wn':pygame.image.load(os.path.join('snake_body', 'body_WN.png')).convert_alpha(),
        'ws':pygame.image.load(os.path.join('snake_body', 'body_WS.png')).convert_alpha(),
        'ne':pygame.image.load(os.path.join('snake_body', 'body_NE.png')).convert_alpha(),
        'nw':pygame.image.load(os.path.join('snake_body', 'body_NW.png')).convert_alpha(),
        'se':pygame.image.load(os.path.join('snake_body', 'body_SE.png')).convert_alpha(),
        'sw':pygame.image.load(os.path.join('snake_body', 'body_SW.png')).convert_alpha()
        }

whole_snake = {'head':head, 'body':body, 'tail':tail}
snakee = snake.Snake(win, (width, height), 15, whole_snake)
foodss  = food.Food(15, 600)
foods_1 = True
not_touch = False
food_infom = 0
#sets our screen size to widht and height
pygame.display.set_caption("Feed_the_Snake")
run = True
clock = pygame.time.Clock()

def food_cordinate(food_check):
    for i in range(1, len(food_check)):
        food_x = random.randint(0, 39)
        food_y = random.randint(0, 39)
        food_x *= 15
        food_y *= 15
        if (food_x in range(food_check[i-1]['x'], food_check[i]['x'])) \
        and (food_y in range(food_check[i-1]['y'], food_check[i]['y'])):    
            continue
        else:
            feed_color = random.choice(list(colors.keys()))
            return {'x': food_x, 'y':food_y, 'col':colors[feed_color]}
while run:
    while game_cont:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_cont = False

    win.fill((10, 10, 10))

    if foods_1:
        food_check = snakee.get_snake()
        food_infom = {'x': 60, 'y':60, 'col':colors['blue']}
        foods_1 = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_cont = True
                break
            if event.key == pygame.K_UP:
                snakee.turn_up_down(down=False)
                break
             
            if event.key == pygame.K_DOWN:
                snakee.turn_up_down()
                break
             
            if event.key == pygame.K_LEFT:
                snakee.turn_left_right(right=False)
                break
             
            if event.key == pygame.K_RIGHT:
                snakee.turn_left_right()
                break
             
        if event.type == pygame.QUIT:
            run = False
            break
    snakee.snake_move()
    # if snakee.get_pos()['x'] == food_infom['x']  and snakee.get_pos()['y'] == food_infom['y']:
    #     tempss = food_infom.copy()
    #     foods_1 = True
    # if foods_1 or not_touch:
    #     not_touch = True
    #     if snakee.get_pos(head=False)['x'] == tempss['x'] and snakee.get_pos(head=False)['y'] == tempss['y']:
    #         not_touch = False
    #         snakee.update_snake(tempss['col'])
    #     pygame.draw.rect(win ,tempss['col'],[tempss['x'], tempss['y'], 7, 7])
    #foodss.update_food(food_infom['col'], win, food_infom['x'], food_infom['y'])      
    pygame.display.update()
    clock.tick(10)
pygame.quit()


