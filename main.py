import sys
import pygame


# Свой курсор мыши
class App:
    def __init__(self):
        self.pos = (0, 0)
        pygame.init()
        pygame.display.set_caption("Свой курсор мыши")
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("data/arrow.png")
        pygame.mouse.set_visible(False)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.pos = event.pos
                    print("Позиция мыши: ", event.pos)

            # Отрисовка фона
            self.screen.fill(pygame.Color("black"))
            self.screen.blit(self.image, self.pos)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
