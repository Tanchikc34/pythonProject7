import sys
import pygame
from random import randrange


# Boom them all
class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Boom them all")
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        for _ in range(20):
            Bomb(self.all_sprites)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.all_sprites.update(event)

            # Отрисовка фона
            self.screen.fill(pygame.Color("black"))
            # Отрисовка кнопок
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(pygame.image.load("data/bomb.png"), (80, 80))
        self.image_boom = pygame.transform.scale(pygame.image.load("data/boom.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, 400)
        self.rect.y = randrange(0, 400)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


if __name__ == '__main__':
    app = App()
    app.run()
