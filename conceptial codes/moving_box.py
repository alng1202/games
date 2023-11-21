import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))
run = True

active_box = None
boxes = []
for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = random.randint(35, 65)
    h = random.randint(35, 65)
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)
def basic_movement(main_player):
    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
        main_player.move_ip(-1,0)
    if key[pygame.K_d] == True:
        main_player.move_ip(1,0)
    if key[pygame.K_w] == True:
        main_player.move_ip(0,-1)
    if key[pygame.K_s] == True:
        main_player.move_ip(0,1)
box = box in boxes

while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    for box in boxes:
        pygame.draw.rect(screen, "purple", box)

    basic_movement(player)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None
        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)

        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()