import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
monitor = pygame.display.set_mode((WIDTH, HEIGHT))

pos_x = 25
pos_y = 25

def move_right():
    global pos_x
    if pos_x + 25 + 20 < WIDTH:
        pos_x += 20

def move_left():
    global pos_x
    if pos_x - 25 - 20 > 0:
        pos_x -= 20

def move_down():
    global pos_y
    if pos_y + 25 + 20 < HEIGHT:
        pos_y += 20

def move_up():
    global pos_y
    if pos_y - 25 - 20 > 0:
        pos_y -= 20

running = True
while running:

    monitor.fill((255, 255, 255))

    pygame.draw.circle(monitor, (255, 0, 0), (pos_x, pos_y), 25)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_UP:
                move_up()

    pygame.display.update()

pygame.quit()
