import pygame, time, random, snake, food

pygame.init()
width  = 490
height = 490
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
snakee = snake.Snake(7, (10, 130, 30), win)
foodss  = food.Food(7, 490)
foods_1 = True
not_touch = False
food_infom = 0
#sets our screen size to widht and height
pygame.display.set_caption("Feed_the_Snake")
run = True
clock = pygame.time.Clock()

def food_cordinate(food_check):
    for i in range(1, len(food_check)):
        food_x = random.randint(0, 69)
        food_y = random.randint(0, 69)
        food_x *= 7
        food_y *= 7
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
        food_infom = food_cordinate(food_check)
        foods_1 = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_cont = True
                break
            if event.key == pygame.K_UP:
                snakee.move_up()
                break
             
            if event.key == pygame.K_DOWN:
                snakee.move_down()
                break
             
            if event.key == pygame.K_LEFT:
                snakee.move_left()
                break
             
            if event.key == pygame.K_RIGHT:
                snakee.move_right()
                break
             
        if event.type == pygame.QUIT:
            run = False
            break
    snakee.snake_move()
    if snakee.get_pos()['x'] == food_infom['x']  and snakee.get_pos()['y'] == food_infom['y']:
        tempss = food_infom.copy()
        foods_1 = True
    if foods_1 or not_touch:
        not_touch = True
        if snakee.get_pos(head=False)['x'] == tempss['x'] and snakee.get_pos(head=False)['y'] == tempss['y']:
            not_touch = False
            snakee.update_snake(tempss['col'])
        pygame.draw.rect(win ,tempss['col'],[tempss['x'], tempss['y'], 7, 7])
    foodss.update_food(food_infom['col'], win, food_infom['x'], food_infom['y'])       
    pygame.display.update()
    clock.tick(15)
pygame.quit()


