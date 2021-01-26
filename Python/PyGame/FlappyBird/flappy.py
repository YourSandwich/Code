import pygame
import random
import sys


class objects:
    def __init__(self):

        self.floor_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/base.png'))
        self.bird_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/bluebird-midflap.png').convert())
        self.bg_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/background-day.png').convert())
        self.pipe_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/pipe-green.png').convert())

        self.bird_rect = self.bird_surface.get_rect(center=(100, 450))

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1200)


class Main:
    def __init__(self):
        self.objects = objects()
        self.screen = screen
        self.pipe_list = []

    def draw_elements(self):
        self.draw_pipes(self.pipe_list)
        self.screen.blit(self.objects.floor_surface, (floor_x_pos, 767))
        self.screen.blit(self.objects.floor_surface, (floor_x_pos+576, 767))
        self.screen.blit(self.objects.bird_surface, object.bird_rect)

    def create_pipe(self):
        new_pipe = self.objects.pipe_surface.get_rect(midtop=(600, 550))
        return new_pipe

    def move_pipes(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 2
        return pipes

    def draw_pipes(self, pipes):
        self.pipe_list = self.move_pipes(main_game.pipe_list)
        for pipe in pipes:
            screen.blit(object.pipe_surface, pipe)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode((576, 900))
pygame.display.set_caption('Flying Birds')
clock = pygame.time.Clock()
main_game = Main()
object = objects()

# Game Variables
gravity = 0.0625
bird_movment = 0
floor_x_pos = 0
floor_y_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movment = 0
                bird_movment -= 5
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == object.SPAWNPIPE:
            main_game.pipe_list.append(main_game.create_pipe())

    bird_movment += gravity
    object.bird_rect.centery += bird_movment
    screen.blit(object.bg_surface, (0, -100))
    floor_x_pos -= 2
    main_game.draw_elements()
    if floor_x_pos <= -576.5:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(240)
