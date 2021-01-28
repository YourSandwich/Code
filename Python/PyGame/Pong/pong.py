import pygame
import sys
import random


class main:
    def draw(self):

        player_text = game_font.render(f"{player_score}", True, light_grey)
        opponent_text = game_font.render(f"{opponent_score}", True, light_grey)

        screen.fill(bg_color)
        screen.blit(player_text, (660, 470))
        screen.blit(opponent_text, (603, 470))
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.aaline(screen, light_grey,
                           (screen_width/2, 0), (screen_width/2, screen_hight))

    def ball_animation(self):
        global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= screen_hight:
            ball_speed_y *= -1
        if ball.left <= 0:
            score_sound.play()
            player_score += 1
            score_time = pygame.time.get_ticks()
        if ball.right >= screen_width:
            score_sound.play()
            opponent_score += 1
            score_time = pygame.time.get_ticks()

        if ball.colliderect(player) and ball_speed_x > 0:
            pong_sound.play()
            if abs(ball.right - player.left) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
                ball_speed_y *= -1
        if ball.colliderect(opponent) and ball_speed_x < 0:
            pong_sound.play()
            if abs(ball.left - opponent.right) < 10:
                ball_speed_x *= -1
            elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
                ball_speed_y *= -1

    def player_animation(self):
        global player_speed
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_hight:
            player.bottom = screen_hight

    def opponent_animation(self):
        global opponent_speed
        opponent.y += opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_hight:
            opponent.bottom = screen_hight

    def ball_restart(self):
        global ball_speed_x, ball_speed_y, score_time
        current_time = pygame.time.get_ticks()
        ball.center = (screen_width/2, screen_hight/2)

        if current_time - score_time < 700:
            number_three = game_font.render("3", True, light_grey)
            screen.blit(number_three, (screen_width/2-10, screen_hight/2+20))
        if 700 < current_time - score_time < 1400:
            number_two = game_font.render("2", True, light_grey)
            screen.blit(number_two, (screen_width/2-10, screen_hight/2+20))
        if 1400 < current_time - score_time < 2100:
            number_one = game_font.render("1", True, light_grey)
            screen.blit(number_one, (screen_width/2-10, screen_hight/2+20))

        if current_time - score_time < 2100:
            ball_speed_x, ball_speed_y = 0, 0
        else:
            ball_speed_y = 2 * random.choice((1, -1))
            ball_speed_x = 2 * random.choice((1, -1))
            score_time = None


pygame.init()
clock = pygame.time.Clock()
main = main()

screen_width = 1280
screen_hight = 960
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('Pong')
game_font = pygame.font.Font('freesansbold.ttf', 32)

player_score = 0
opponent_score = 0

score_time = True

ball = pygame.Rect(screen_width/2-15, screen_hight/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_hight/2-70, 10, 140)
opponent = pygame.Rect(10, screen_hight/2-70, 10, 140)

ball_speed_x = 2 * random.choice((1, -1))
ball_speed_y = 2 * random.choice((1, -1))

player_speed = 0
opponent_speed = 0

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Sound
pong_sound = pygame.mixer.Sound(
    '/mnt/Data/Müll/Code/Python/PyGame/Pong/pong.wav')
score_sound = pygame.mixer.Sound(
    "/mnt/Data/Müll/Code/Python/PyGame/Pong/score.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
            if event.key == pygame.K_s:
                opponent_speed += 5
            if event.key == pygame.K_w:
                opponent_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5
            if event.key == pygame.K_s:
                opponent_speed -= 5
            if event.key == pygame.K_w:
                opponent_speed += 5

    main.draw()
    if score_time:
        main.ball_restart()
    main.ball_animation()
    main.player_animation()
    main.opponent_animation()

    pygame.display.update()
    clock.tick(240)
