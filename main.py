import pygame, time, random, snake, food

pygame.init()
width  = 490
height = 490
feed_color = "asd"
foodss_1 = True
foodss_2 = False
food_act = 0
colors = {
    'blue'   : (0, 0, 255),
    'red'    : (255, 0, 0),
    'green'  : (0,255, 0),
    'orange' : (255, 255, 0),
    'purple' : (0, 255, 255),
    'pink'   : (255, 0, 255),
    'white'  : (255, 255, 255)
}
win    = pygame.display.set_mode((width, height))
snakee = snake.Snake(7, (10, 130, 30), win)
foods_1  = food.Food(7, 490)
foods_2  = food.Food(7, 490)
food_active = [foods_1, foods_2]
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
            return {'food_x': food_x, 'food_y':food_y, 'food_col':colors[feed_color]}

while run:
    win.fill((40, 40, 40))
    if foods_1:
        food_check = snakee.get_snake()
        food_1 = food_cordinate(food_check)
        foods_1 = False

    if foods_2:
        food_check = snakee.get_snake()
        food_2 = food_cordinate(food_check)
        foods_2 = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakee.move_up()
                break
                #print(snakee.get_head())
            if event.key == pygame.K_DOWN:
                snakee.move_down()
                break
                #print(snakee.get_head())
            if event.key == pygame.K_LEFT:
                snakee.move_left()
                break
                #print(snakee.get_head())
            if event.key == pygame.K_RIGHT:
                snakee.move_right()
                break
                #print(snakee.get_head())
        if event.type == pygame.QUIT:
            run = False
            break
    #snakee.draw_snake(win)
    if snakee.get_pos()['x'] == food_x and snakee.get_pos()['y'] == food_y:
        foods_2 = True
    if snakee.get_pos(head=False)['x'] == food_x and snakee.get_pos(head=False)['y'] == food_y:
        snakee.update_snake(colors[feed_color])
        foodss_1 = True      
    snakee.snake_move()
    if foods_2:
        foods_1.update_food(food_1['color'], win, food_1['food_x'], food_1['food_y'])
    foods_2.update_food(colors[feed_color], win, food_x[0], food_y[0])
    pygame.display.update()
    clock.tick(15)
pygame.quit()


