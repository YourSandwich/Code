import pygame

#from pygame.locals import *

#--------------------------------------------------------------------
# class for single sprite
#--------------------------------------------------------------------

class MySprite():

    def __init__(self, image, x, y):

        self.image = pygame.image.load(image)
        image_rect = self.image.get_rect()

        # Rect class to use "Sprite collision detect" - in the future
        # In rect you have sprite position and size
        # You can use self.rect.x, self.rect.y, self.rect.width, self.rect.height
        # and self.rect.center, self.rect.centerx, self.rect.top, self.rect.bottomright etc.

        self.rect = pygame.rect.Rect(x, y, image_rect.width, image_rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


#--------------------------------------------------------------------
# class for player
#--------------------------------------------------------------------

class MyPlayer(MySprite):

    def __init__(self, image, x, y):
        # parent constructor always as a first in __init__
        MySprite.__init__(self, image, x, y)

        self.speed_x = self.speed_y = 0

    #-----------------------------

    def set_speed(self, x, y):
        self.speed_x = x
        self.speed_y = y

    #-----------------------------

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.centerx < 0 :
            self.rect.centerx = 800
        elif self.rect.centerx > 800 :
            self.rect.centerx = 0

        if self.rect.centery < 0 :
            self.rect.centery = 600
        elif self.rect.centery > 600 :
            self.rect.centery = 0

#--------------------------------------------------------------------

class Window():

    def __init__(self, width, height):

        #--------------------
        self.rect = pygame.Rect(0, 0, width, height)
        # or
        self.width, self.height = width, height
        #--------------------

        pygame.init()

        # most users and tutorials call it "screen"
        self.screen = pygame.display.set_mode(self.rect.size)

        #############################################################

        self.foreground = None
        self.background = None

        self.set_background("background.jpg")
        self.set_foreground("ball3.png")

        #################################################

        self.player = MyPlayer("ball1.png", 100, 200)

        self.sprites_list = []

        self.add_sprite(MySprite("ball2.png", 100, 400))
        self.add_sprite(MySprite("ball2.png", 300, 500))
        self.add_sprite(MySprite("ball2.png", 300, 200))

        self.remove_last_sprite()

        #-----------------------------

        # red text "PAUSE"
        font = pygame.font.SysFont("", 72)
        self.text_pause = font.render("PAUSE", True, (255, 0, 0))

        # center text on screen
        screen_center = self.screen.get_rect().center
        self.text_pause_rect = self.text_pause.get_rect(center=screen_center)

    #--------------------------

    def add_sprite(self, sprite):
        self.sprites_list.append(sprite)

    #--------------------------

    def remove_last_sprite(self):
        if self.sprites_list:
            del self.sprites_list[-1]

    #--------------------------

    def draw_sprites(self, screen):
        for sprite in self.sprites_list:
            sprite.draw(screen)

    #--------------------------

    def draw_background(self, screen):
        screen.fill((0,64,0)) # clear screen to green
        if self.background:
            screen.blit(self.background, (0,0))

    #--------------------------

    def draw_foreground(self, screen):
        if self.foreground:
            screen.blit(self.foreground, (0,0))

    #--------------------------

    def draw_world(self, image):
        temp = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image_rect = image.get_rect()

        for x in range(0, self.rect.width, 60):
            for y in range(0,self.rect.width, 60):
                temp.blit(image,(x,y))

        return temp

    #--------------------------

    def set_foreground(self, image=None):
        if image:
            img = pygame.image.load(image)
            self.foreground = self.draw_world(img)

    #--------------------------

    def set_background(self, image=None):
        if image:
            self.background = pygame.image.load(image)

    #--------------------------

    def run(self):

        clock = pygame.time.Clock()

        RUNNING = True
        PAUSED = False

        while RUNNING:

            #--- events ---

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUNNING = False
                    elif event.key == pygame.K_SPACE:
                        PAUSED = not PAUSED

                    if event.key == pygame.K_UP:
                        self.player.set_speed(0,-10)
                    elif event.key == pygame.K_DOWN:
                        self.player.set_speed(0,10)
                    elif event.key == pygame.K_LEFT:
                        self.player.set_speed(-10,0)
                    elif event.key == pygame.K_RIGHT:
                        self.player.set_speed(10,0)

                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                        self.player.set_speed(0,0)

            #--- changes ----

            if not PAUSED:
                # change elements position
                self.player.update()

            #--- draws ---

            self.draw_background(self.screen)
            self.draw_foreground(self.screen)
            self.draw_sprites(self.screen)
            self.player.draw(self.screen)

            if PAUSED:
                # draw pause string
                self.screen.blit(self.text_pause, self.text_pause_rect.topleft)

            pygame.display.update()

            #--- FPS ---

            clock.tick(25) # 25 Frames Per Seconds

        #--- finish ---

        pygame.quit()

#----------------------------------------------------------------------

Window(800,600).run()
