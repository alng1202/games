import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WALL_THICKNESS = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, SCREEN_HEIGHT), WALL_THICKNESS)
    right = pygame.draw.line(screen, 'white', (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    top = pygame.draw.line(screen, 'white', (0, 0), (SCREEN_WIDTH, 0), WALL_THICKNESS)
    bottom = pygame.draw.line(screen, 'white', (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    wall_list = [left, right, top, bottom]

    return wall_list

while running:
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")
    walls = draw_walls()

    # RENDER GAME HERE

    player = pygame.draw.circle(screen, "blue", player_pos, 10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 50
    if keys[pygame.K_s]:
        player_pos.y += 50
    if keys[pygame.K_a]:
        player_pos.x -= 50
    if keys[pygame.K_d]:
        player_pos.x += 50

    # flip() the display to present work on screen
    pygame.display.flip()

    clock.tick(FPS) # limits FPS to 60

pygame.quit()