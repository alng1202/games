import pygame
import pygame.freetype
import random


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WALL_THICKNESS = 10

BAR_WIDTH = 10
BAR_HEIGHT = 100

BALL_RADIUS = 25
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
BALL_MODE = random.randint(1, 4)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True

player_1 = pygame.Rect(10, (SCREEN_HEIGHT/2) - (BAR_HEIGHT/2), BAR_WIDTH, BAR_HEIGHT)
player_2 = pygame.Rect((SCREEN_WIDTH - 22) - (BAR_WIDTH/2), (SCREEN_HEIGHT/2) - (BAR_HEIGHT/2), BAR_WIDTH, BAR_HEIGHT)

ball = pygame.Rect(SCREEN_WIDTH/2 - BALL_RADIUS/2, SCREEN_HEIGHT/2 - BALL_RADIUS/2, BALL_RADIUS, BALL_RADIUS)

def ball_collision():
    global BALL_SPEED_X, BALL_SPEED_Y, BALL_MODE

    ## randomizes ball starting direction
    if BALL_MODE == 1:
        ball.x += BALL_SPEED_X
        ball.y += BALL_SPEED_Y
    elif BALL_MODE == 2:
        ball.x -= BALL_SPEED_X
        ball.y += BALL_SPEED_Y
    elif BALL_MODE == 3:
        ball.x += BALL_SPEED_X
        ball.y -= BALL_SPEED_Y
    else:
        ball.x -= BALL_SPEED_X
        ball.y -= BALL_SPEED_Y

    ## border collision
    if ball.right >= SCREEN_WIDTH or ball.left <= 0:
        BALL_SPEED_X = 3
        BALL_SPEED_Y = 3

        ball.x = SCREEN_WIDTH/2 - BALL_RADIUS/2
        ball.y = SCREEN_HEIGHT/2 - BALL_RADIUS/2

        player_1.x = 10
        player_1.y = (SCREEN_HEIGHT/2) - (BAR_HEIGHT/2)

        player_2.x = (SCREEN_WIDTH - 23) - (BAR_WIDTH/2)
        player_2.y = (SCREEN_HEIGHT/2) - (BAR_HEIGHT/2)

        pygame.time.wait(200)
        
    if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
        BALL_SPEED_Y *= -1
    
    ## player-ball collision using obj1.colliderect(obj2)
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        BALL_SPEED_X *= -1
        ## ball speeds up every deflection by player
        if BALL_SPEED_X < 0:
            BALL_SPEED_X -= 0.5
            BALL_SPEED_Y -= 0.5
        else:
            BALL_SPEED_X += 0.5
            BALL_SPEED_Y += 0.5

def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, SCREEN_HEIGHT), WALL_THICKNESS)
    right = pygame.draw.line(screen, 'white', (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    top = pygame.draw.line(screen, 'white', (0, 0), (SCREEN_WIDTH, 0), WALL_THICKNESS)
    bottom = pygame.draw.line(screen, 'white', (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    wall_list = [left, right, top, bottom]

def basic_movement(main_player, type):
    key = pygame.key.get_pressed()
    
    if type == "wasd":
        if key[pygame.K_w] == True:
            main_player.move_ip(0,-10)
        if key[pygame.K_s] == True:
            main_player.move_ip(0,10)
    else:
        if key[pygame.K_UP] == True:
            main_player.move_ip(0,-10)
        if key[pygame.K_DOWN] == True:
            main_player.move_ip(0,10)

class Score(object):
    def __init__(self):
        self.count = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = self.font.render(str(self.count), True, "white")

    def score_up(self):
        self.count += 1
        self.text = self.font.render("Score : " + str(self.count), 1, "black")

    def show_score(self):
        screen.blit(self.text, (SCREEN_WIDTH/2 - 60 , 40))
    
while running:
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    # RENDER GAME HERE
    pygame.draw.aaline(screen, "gray", (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), player_1)
    pygame.draw.rect(screen, (255, 0, 0), player_2)
    pygame.draw.ellipse(screen, "gray", ball)

    basic_movement(player_1, "wasd")
    basic_movement(player_2, "arrow")

    ball_collision()

    draw_walls()

    # PLAYER_1_SCORE = SCORE_FONT.render("0", True, "white")
    # screen.blit(PLAYER_1_SCORE, (SCREEN_WIDTH/2 - 60, 40))
    # PLAYER_2_SCORE = SCORE_FONT.render("0", True, "white")
    # screen.blit(PLAYER_1_SCORE, (SCREEN_WIDTH/2 + 40, 40))

    # flip() the display to present work on screen
    pygame.display.flip()

    clock.tick(FPS) # limits FPS to 60

pygame.quit()