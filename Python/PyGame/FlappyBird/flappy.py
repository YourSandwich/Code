import pygame
import random
import sys


class objects:
    def __init__(self):

        self.floor_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/base.png')).convert()
        self.bg_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/background-day.png').convert())
        self.pipe_surface = pygame.transform.scale2x(
            pygame.image.load('Textures/pipe-green.png').convert())

        self.bird_downflap = pygame.transform.scale2x(
            pygame.image.load('Textures/bluebird-downflap.png').convert_alpha())
        self.bird_midflap = pygame.transform.scale2x(
            pygame.image.load('Textures/bluebird-midflap.png').convert_alpha())
        self.bird_upflap = pygame.transform.scale2x(
            pygame.image.load('Textures/bluebird-upflap.png').convert_alpha())
        self.bird_frames = [self.bird_downflap,
                            self.bird_midflap, self.bird_upflap]
        self.bird_index = 0
        self.bird_surface = self.bird_frames[self.bird_index]
        self.bird_rect = self.bird_surface.get_rect(center=(100, 450))

        self.game_over_surface = pygame.transform.scale2x(pygame.image.load(
            'Textures/message.png')).convert_alpha()
        self.game_over_rect = self.game_over_surface.get_rect(
            center=(288, 450))

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1200)


class Main:
    def __init__(self):
        self.objects = objects()
        self.screen = screen
        self.pipe_list = []
        self.pipe_height = [500, 540, 400, 600, 450, 380]

    def draw_elements(self):
        self.draw_pipes(self.pipe_list)
        self.screen.blit(self.objects.floor_surface, (floor_x_pos, 767))
        self.screen.blit(self.objects.floor_surface, (floor_x_pos+579, 767))
        self.screen.blit(rotated_bird, object.bird_rect)

    def create_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.objects.pipe_surface.get_rect(
            midtop=(700, random_pipe_pos))
        top_pipe = self.objects.pipe_surface.get_rect(
            midbottom=(700, random_pipe_pos-300))
        return bottom_pipe, top_pipe

    def move_pipes(self, pipes):
        visible_pipes = [pipe for pipe in pipes if pipe.right > -50]
        if game_active:
            for pipe in pipes:
                pipe.centerx -= 2
            return visible_pipes
        else:
            for pipe in pipes:
                pipes == 0
            return visible_pipes

    def draw_pipes(self, pipes):
        self.pipe_list = self.move_pipes(main_game.pipe_list)
        for pipe in pipes:
            if pipe.bottom >= 900:
                screen.blit(object.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(
                    object.pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def collision(self, pipes):
        for pipe in pipes:
            global can_score
            if object.bird_rect.colliderect(pipe):
                can_score = False
                return False

        if object.bird_rect.top <= -20 or object.bird_rect.bottom >= 767:
            return False
            can_score = False
        return True

    def rotate_bird(self, bird):
        new_bird = pygame.transform.rotozoom(
            object.bird_surface, -bird_movment * 3, 1)
        return new_bird

    def bird_animation(self):
        new_bird = object.bird_frames[object.bird_index]
        new_bird_rect = new_bird.get_rect(
            center=(100, object.bird_rect.centery))
        return new_bird, new_bird_rect

    def pipe_score_check(self):
        global score, can_score

        if self.pipe_list:
            for pipe in self.pipe_list:
                if 95 < pipe.centerx < 105 and can_score:
                    score += 1
                    score_sound.play()
                    can_score = False
                if pipe.centerx < 70:
                    can_score = True

    def score_display(self, game_state):
        if game_state == 'main_game':
            score_surface = game_font.render(
                str(int(score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(
                f'Score: {int(score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(
                f'High score: {int(high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(288, 850))
            screen.blit(high_score_surface, high_score_rect)

    def update_score(self, score, high_score):
        if score > high_score:
            high_score = score
        return high_score


pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode((576, 900))
pygame.display.set_caption('Flying Bird')
clock = pygame.time.Clock()
main_game = Main()
object = objects()
game_font = pygame.font.Font('04B_19__.TTF', 40)

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# Game Variables
game_active = True
gravity = 0.0625
bird_movment = 0
floor_x_pos = 0
floor_y_pos = 0

# Score
score = 0
high_score = 0
can_score = True

# Sound
help = True
flap_sound = pygame.mixer.Sound('Audio/SFX/sfx_wing.wav')
death_sound = pygame.mixer.Sound('Audio/SFX/sfx_hit.wav')
score_sound = pygame.mixer.Sound('Audio/SFX/sfx_point.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                flap_sound.play()
                bird_movment = 0
                bird_movment -= 5
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                help = True
                main_game.pipe_list.clear()
                object.bird_rect.center = (100, 412)
                score = 0
                can_score = True
                bird_movment = -3

        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == object.SPAWNPIPE:
            main_game.pipe_list.extend(main_game.create_pipe())
        if event.type == BIRDFLAP:
            if object.bird_index < 2:
                object.bird_index += 1
            else:
                object.bird_index = 0
            object.bird_surface, object.bird_rect = main_game.bird_animation()
    if game_active:
        rotated_bird = main_game.rotate_bird(object.bird_surface)
        bird_movment += gravity
        object.bird_rect.centery += bird_movment
        if floor_x_pos <= -576.5:
            floor_x_pos = 0
        floor_x_pos -= 2
    screen.blit(object.bg_surface, (0, -100))
    game_active = main_game.collision(main_game.pipe_list)
    main_game.draw_elements()
    main_game.pipe_score_check()
    if game_active:
        main_game.score_display('main_game')
    else:
        high_score = main_game.update_score(score, high_score)
        main_game.score_display('game_over')
        screen.blit(object.game_over_surface, object.game_over_rect)
        if help:
            death_sound.play()
        help = False
    pygame.display.update()
    clock.tick(240)
