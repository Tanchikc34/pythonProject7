import sys
import pygame


# Герой двигается!
class App:
    def __init__(self):
        self.x = 0
        self.y = 0
        pygame.init()
        pygame.display.set_caption("Герой двигается!")
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("data/creature.png")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        self.x += 10
                    elif event.key == pygame.K_UP:
                        self.y -= 10
                    elif event.key == pygame.K_DOWN:
                        self.y += 10

            # Отрисовка фона
            self.screen.fill(pygame.Color("white"))
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
