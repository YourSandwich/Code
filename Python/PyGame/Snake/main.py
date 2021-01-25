import pygame
import sys
import random
import re
from pygame.math import Vector2

# TODO: Implement menu for Retry and Quit


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        # Textures
        self.head_up = pygame.image.load(
            'Texture/head.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Texture/headD.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Texture/headL.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Texture/headR.png').convert_alpha()

        self.tail_up = pygame.image.load(
            'Texture/tailU.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Texture/tailD.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Texture/tailL.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Texture/tailR.png').convert_alpha()

        self.bend_right = pygame.image.load(
            'Texture/bendR.png').convert_alpha()  # right
        self.bend_left = pygame.image.load(
            'Texture/bendL.png').convert_alpha()  # right
        self.bend_up = pygame.image.load(
            'Texture/bendU.png').convert_alpha()  # dont show up
        self.bend_down = pygame.image.load(
            'Texture/bendD.png').convert_alpha()  # right

        self.body_vertical = pygame.image.load(
            'Texture/body.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Texture/bodyH.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound(
            'Audio/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # 1. Rect for the position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # Head lokks in what position
            if index == 0:
                display.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                display.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    display.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    display.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        display.blit(self.bend_right, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        display.blit(self.bend_left, block_rect)
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        display.blit(self.bend_up, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        display.blit(self.bend_down, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

        # for block in self.body:
        #     # create rectangle and draw it
        #     x_pos = int(block.x*cell_size)
        #     y_pos = int(block.y*cell_size)
        #     block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        #     pygame.draw.rect(display, (137, 255, 130), block_rect)

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up

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

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        # draw a rectangle
        fruit_rect = pygame.Rect(
            int(self.pos.x) * cell_size, int(self.pos.y)*cell_size, cell_size, cell_size)
        # pygame.draw.rect(display, (255, 7, 7), fruit_rect) draw rectangle
        display.blit(cherry, fruit_rect)  # Draws Grpahics

    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        # Create a Vector with 2 Options
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # New Fruit
            # Make Snake longer
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        # Is snake outsie of the screen?
        # Check if snake hit himself
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_grass(self):
        grass_color = (97, 180, 8)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display, grass_color, grass_rect)

    def draw_score(self):
        with open('highscore.txt', mode='r+', encoding='UTF-8', errors='strict')as file:
            global score_text
            score_text = str(len(self.snake.body) - 3)
            score_surface = game_font.render(score_text, True, (54, 74, 12))
            score_x = int(cell_size * cell_number - 60)
            score_y = int(cell_size*cell_number - 40)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            cherry_rect = cherry.get_rect(
                midright=(score_rect.left, score_rect.centery))
            bg_rect = pygame.Rect(cherry_rect.left-6, cherry_rect.top-6,
                                  cherry_rect.width + 6 + score_rect.width + 6, cherry_rect.height+12)

            pygame.draw.rect(display, (167, 209, 61), bg_rect)
            display.blit(score_surface, score_rect)
            display.blit(cherry, cherry_rect)
            pygame.draw.rect(display, (54, 74, 12), bg_rect, 2)
        # Highscore
            hscore_text = "highscore: " + str(file.readlines()).strip("'[]'")
            hscore_surface = game_font.render(hscore_text, True, (34, 54, 12))
            hscore_x = int(cell_size * cell_number-cell_number*cell_size + 40)
            hscore_y = int(cell_number*cell_size-cell_number*cell_size + 60)
            hscore_rect = hscore_surface.get_rect(
                center=(hscore_x + 75, hscore_y))
            h_rect = pygame.Rect(hscore_rect.left-6, hscore_rect.top-6,
                                 hscore_rect.width + 12, hscore_rect.height+12)
            pygame.draw.rect(display, (0, 0, 0), h_rect, 2)
            display.blit(hscore_surface, hscore_rect)

    def game_over(self):
        save()
        self.snake.reset()


def save():
    with open('highscore.txt', mode='r') as file:
        data = file.read()
    if int(score_text) >= int(data):
        with open('highscore.txt', mode='r+')as file:
            file.write(score_text)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
pygame.display.set_caption('Pythonistas Snake')
display = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()  # Set the speed of the Game
cherry = pygame.image.load(
    'Texture/cherry2.png').convert_alpha()
game_font = pygame.font.Font(
    '/home/sandwich/Müll/Code/Python/Assets/Fonts/PinkChicken-Regular.ttf', 31)

DISPLAY_UPDATE = pygame.USEREVENT
pygame.time.set_timer(DISPLAY_UPDATE,  150)

main_game = MAIN()

# In this Loop are all our elements / Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == DISPLAY_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
    display.fill((98, 184, 8))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(240)
