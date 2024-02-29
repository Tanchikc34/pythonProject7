import sys
import pygame


# Game over
class App:
    def __init__(self):
        self.pos = (0, 0)
        pygame.init()
        pygame.display.set_caption("Game over")
        self.screen = pygame.display.set_mode((600, 300))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("data/gameover.png")
        self.im_x, self.im_y = -600, 0
        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Sprite(self.all_sprites)
        self.car.image = self.image
        self.car.rect = self.car.image.get_rect()
        self.car.rect.x = self.im_x
        self.car.rect.y = self.im_y
        self.speed = 2

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.car.update()
            self.all_sprites.draw(self.screen)

            if self.im_x + self.car.rect.width == 600:
                self.speed = 0
            if self.im_x < 0:
                self.speed = 2

            all_sprites = pygame.sprite.Group()
            car = pygame.sprite.Sprite(all_sprites)

            if self.speed == 2:
                car.image = self.image
                car.rect = car.image.get_rect()
            else:
                car.image = self.image
                car.rect = car.image.get_rect()

            self.im_x += self.speed
            car.rect.x = self.im_x
            car.rect.y = self.im_y
            car.update()

            self.screen.fill(pygame.Color('blue'))
            all_sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
