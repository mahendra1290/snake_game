import pygame, os, time, random, snake, food, font

FPS = 10
main_direct = 'snakes'
pygame.init()
width  = 600
height = 600
black = (0, 0, 0)
score = 0
feed_color = "asd"
food_infom = 0
tempss = 0
game_cont  = False
game_start = True
game_over  = False
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
pygame.display.set_icon(pygame.image.load(os.path.join('snakes\snake_1\snake_head', 'head_W.png')).convert_alpha())

def snake_loader(mainpath, snake_no):
    snake = {'head':{}, 'body':{}, 'tail':{}}
    snake_direc = {
                'head' : ['e', 'n', 's', 'w'],
                'tail' : ['e', 'n', 's', 'w'],
                'body' : ['e', 'en', 'es', 'n', 'ne', 'nw', 's', 'se', 'sw', 'w', 'wn', 'ws']
    }
    snakes_list = os.listdir(mainpath)
    temp = os.path.join(mainpath, snakes_list[snake_no])
    snake_part = os.listdir(temp)
    print(snake_part)
    snake_key = list(snake.keys())
    snake_key.sort()
    for i, v in zip(snake_part, snake_key):
        part_path = os.path.join(temp, i)
        part = os.listdir(part_path)
        for j in range(len(part)):
            abs_path = os.path.join(part_path, part[j])
            snake[v].update({snake_direc[v][j]:pygame.image.load(abs_path).convert_alpha()})
    return snake

whole_snake = snake_loader(main_direct, 2)
snakee = snake.Snake(win, (width, height), 15, whole_snake)
foodss  = food.Food(15, 600)
foods_1 = True
not_touch = False
food_infom = 0
#sets our screen size to widht and height
pygame.display.set_caption("Feed_the_Snake")
run = True
clock = pygame.time.Clock()
start = pygame.image.load('temp\start.png').convert_alpha()
game = pygame.image.load('temp\game.fw.png').convert_alpha()
def food_cordinate(food_check):
    not_get_food = True
    while not_get_food:
        food_x = random.randint(0, 39)
        food_y = random.randint(0, 39)
        food_x *= 15
        food_y *= 15
        get = True
        for i in food_check:
            if food_x ==  i['x'] and food_y == i['y']:
                print("on snake")
                get = False
                break
        if get:
            feed_color = random.choice(list(colors.keys()))
            not_get_food = False
            return {'x': food_x, 'y':food_y, 'col':colors[feed_color]}

main_text = font.Text('temp\comic.ttf', 30, win)
flash_text  = font.Flash_text('temp\comic.ttf', 40, win)
while run:
    while game_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_start = False
                break
            #z = pygame.mouse.get_pos()
            #print(z)
        win.blit(start, (0,0))
        if flash_text.draw("Play", colors['orange'], colors['red'], (115, 325)):
            game_start = False
            break
        flash_text.draw("Options", colors['blue'], colors['white'], (80, 460))
        pygame.display.update()
        clock.tick(FPS)
    win.blit(game, (0, 0))
    while game_cont:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_cont = False

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

    if foods_1:
        food_check = snakee.get_snake()
        food_detail = food_cordinate(food_check)
        foods_1 = False

    if snakee.is_collision(food_detail['x'], food_detail['y']):
        score += 1
        snakee.update_snake()
        foods_1 = True

    foodss.update_food(food_detail['col'], win, food_detail['x'], food_detail['y'])
    snakee.snake_move() 
    if snakee.self_collision():
        game_cont = True
    main_text.draw("Score "+str(score), black, (5, 5))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()


