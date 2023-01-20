import pygame


class Window():
    def __init__(self):

        pygame.init()


        windowSize = pygame.display.get_desktop_sizes()
        windowX, windowY = windowSize[1]
        windowX = windowX * 0.45
        windowY = windowY * 0.8

        self.screen = pygame.display.set_mode((windowX, windowY))
        pygame.display.set_caption('Chess')

        self.tiles_list = ['1','2']


    def draw_background(self, screen):
        screen.fill((157, 151, 118)) # clear screen to green

    def draw_tiles(self, screen):
        x,y = screen.get_size()

        size = x / 8.8
        number = 8
        color = (111, 74, 49)
        for row in range(number):
            if row % 2 == 0:
                for col in range(number):
                    if col % 2 != 0:
                        rect = pygame.Rect(
                            col * size + 40, row * size + 40, size, size)
                        pygame.draw.rect(screen, color, rect)
            else:
                for col in range(number):
                    if col % 2 == 0:
                        rect = pygame.Rect(
                            col * size + 40, row * size + 40, size, size)
                        pygame.draw.rect(screen, color, rect)

    def run(self):
        clock = pygame.time.Clock()

        RUNNING = True

        while RUNNING:
            #--- events ---


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

                #--- draws ---

                self.draw_background(self.screen)
                self.draw_tiles(self.screen)


                #--- FPS ---
                pygame.display.update()
                clock.tick(240)

        #--- finish ---

        pygame.quit()

#----------------------------------------------------------------------





Window().run()
