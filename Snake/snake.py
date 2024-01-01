## Alan Nguyen

""" 
Abstract of snake:
    - The snake moves on a grid map
    - Each box on the grid map is defined as a cell.
"""



import pygame, sys, random
from pygame.math import Vector2

pygame.init()

CELL_SIZE = 40
CELL_NUMBER = 20
FPS = 60

screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 25)

class FRUIT:
    def __init__(self):
        # create an x and y position
        # draw a square

        self.randomize()
        
        # Vector2 takes in an x and y, and returns a coordinate value (x, y)

    def draw_fruit(self):
        x_pos = self.pos.x * CELL_SIZE
        y_pos = self.pos.y * CELL_SIZE
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        # self.pos.x/y refers to the corresponding coordinate value of the Vector: x or y 
        pygame.draw.rect(screen, "red", fruit_rect)
        # draw rectangle
    
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, 19)
        self.pos = pygame.math.Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            # create a rect
            # draw the rectangle

            x_pos = block.x * CELL_SIZE
            y_pos = block.y * CELL_SIZE

            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "blue", snake_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        # heck if snake collides with fruit
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # check if snake goes out of bounds
        if (not 0 <= self.snake.body[0].x < CELL_NUMBER) or (not 0 <= self.snake.body[0].y < CELL_NUMBER):
            self.game_over()

        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_x = int(CELL_NUMBER * CELL_SIZE - 60)
        score_y = int(CELL_NUMBER * CELL_SIZE - 40)

        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        bg_rect = pygame.Rect(score_rect.left, score_rect.top, score_rect.width, score_rect.height)
        
        pygame.draw.rect(screen, (167,209,61), bg_rect)
        screen.blit(score_surface, score_rect)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)

    ## RENDER GAME HERE
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(FPS)
    
    