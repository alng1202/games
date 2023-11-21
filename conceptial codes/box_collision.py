import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

clock = pygame.time.Clock()

moving_rect = pygame.Rect(350, 350, 100, 100)

x_speed = 5
y_speed = 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

def bouncing_rect():
    global x_speed, y_speed
    
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    pygame.draw.rect(screen, (255, 0, 0), moving_rect)
    pygame.draw.rect(screen, (255, 255, 255), other_rect)

    # collision with screen border
    if moving_rect.right >= SCREEN_WIDTH or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= SCREEN_WIDTH or moving_rect.top <= 0:
        y_speed *= -1

    # collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance:
            x_speed *= -1
while run:
    screen.fill((3, 7, 40))
    bouncing_rect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(100)
pygame.quit()