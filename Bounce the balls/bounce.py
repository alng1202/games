import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

# game variables
running = True
WALL_THICKNESS = 10
gravity = 0.5
bounce_stop = 0.3
# track position of mouse to get movement vector
mouse_trajectory = []

# player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, x_speed, y_speed, id, friction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.id = id
        self.circle = ''
        self.selected = False
        self.friction = friction

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if not self.selected:
            if self.y_pos < SCREEN_HEIGHT - self.radius - (WALL_THICKNESS/2):
                self.y_speed += gravity
            else:
                if self.y_speed > bounce_stop:
                    self.y_speed = self.y_speed * -1 * self.retention
                else:
                    if abs(self.y_speed) <= bounce_stop:
                        self.y_speed = 0
            if (self.x_pos < self.radius + (WALL_THICKNESS/2) and self.x_speed < 0) or \
                  (self.x_pos > SCREEN_WIDTH - self.radius - (WALL_THICKNESS/2) and self.x_speed > 0):
                self.x_speed *= -1 * self.retention
                if abs(self.x_speed) < bounce_stop:
                    self.x_speed = 0
            if self.y_speed == 0 and self.x_speed != 0:
                if self.x_speed > 0:
                    self.x_speed -= self.friction
                elif self.x_speed < 0:
                    self.x_speed += self.friction
        else:
            self.x_speed = x_push
            self.y_speed = y_push
        return self.y_speed
    
    def update_pos(self, mouse):
        if not self.selected:
            self.y_pos += self.y_speed
            self.x_pos += self.x_speed
        else:
            self.x_pos = mouse[0]
            self.y_pos = mouse[1]

    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected

def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, SCREEN_HEIGHT), WALL_THICKNESS)
    right = pygame.draw.line(screen, 'white', (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    top = pygame.draw.line(screen, 'white', (0, 0), (SCREEN_WIDTH, 0), WALL_THICKNESS)
    bottom = pygame.draw.line(screen, 'white', (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), WALL_THICKNESS)
    wall_list = [left, right, top, bottom]

    return wall_list

def calc_motion_vector():
    x_speed = 0
    y_speed = 0

    if len(mouse_trajectory) > 10:
        x_speed = (mouse_trajectory[-1][0] - mouse_trajectory[0][0]) / len(mouse_trajectory)
        y_speed = (mouse_trajectory[-1][1] - mouse_trajectory[0][1]) / len(mouse_trajectory)

    return x_speed, y_speed

ball1 = Ball(50, 50, 30, "blue", 100, .8, 0, 0, 1, 0.02)
ball2 = Ball(500, 500, 50, "green", 300, .9, 0, 0, 2, 0.03)
ball3 = Ball(200, 200, 40, "purple", 200, .8, 0, 0, 3, 0.04)
balls = [ball1, ball2, ball3]
active_select = False

while running:
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for ball in balls:
                    if ball.check_select(event.pos):
                        active_select = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                for i in range(len(balls)):
                    balls[i].check_select((-1000, -1000)) # give a coord. value that is always false

    
    screen.fill("black")
    walls = draw_walls()
    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    
    if len(mouse_trajectory) > 20: 
        mouse_trajectory.pop(0)

    x_push, y_push = calc_motion_vector()

    for ball in balls:
        ball.draw()
        ball.update_pos(mouse_coords)
        ball.y_speed = ball.check_gravity()

    # RENDER GAME HERE

    # player = pygame.draw.circle(screen, "blue", player_pos, 10)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 50
    # if keys[pygame.K_s]:
    #     player_pos.y += 50
    # if keys[pygame.K_a]:
    #     player_pos.x -= 50
    # if keys[pygame.K_d]:
    #     player_pos.x += 50

    # flip() the display to present work on screen
    pygame.display.flip()

    clock.tick(FPS) # limits FPS to 60

pygame.quit()