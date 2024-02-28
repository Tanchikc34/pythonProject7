import sys
import pygame


# Машинка
class App:
    def __init__(self):
        self.pos = (0, 0)
        pygame.init()
        pygame.display.set_caption("Машинка")
        self.screen = pygame.display.set_mode((600, 95))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("data/car2.png")
        self.im_x, self.im_y = 0, 0
        self.all_sprites = pygame.sprite.Group()
        self.car = pygame.sprite.Sprite(self.all_sprites)
        self.car.image = self.image
        self.car.rect = self.car.image.get_rect()
        self.car.rect.x = self.im_x
        self.car.rect.y = self.im_y
        self.speed = 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.car.update()
            self.all_sprites.draw(self.screen)

            if self.im_x + self.car.rect.width == 600:
                speed = -1
            if self.im_x == 0:
                speed = 1
            all_sprites = pygame.sprite.Group()
            car = pygame.sprite.Sprite(all_sprites)
            if speed == 1:
                car.image = self.image
                car.rect = car.image.get_rect()
            else:
                car.image = pygame.transform.flip(self.image, True, False)
                car.rect = car.image.get_rect()

            self.im_x += speed
            car.rect.x = self.im_x
            car.rect.y = self.im_y
            car.update()

            self.screen.fill(pygame.Color('white'))
            all_sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()
