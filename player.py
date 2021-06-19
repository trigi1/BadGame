from bullet import Bullet
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 480
        self.overflowY = 0
        self.overflowX = 0

    def create_bullet(self, img, x, y, ax, ay):
        return Bullet(img, x, y, ax, ay)

    def up(self, num):
        self.overflowY -= num
        if self.overflowY < 0:
            self.rect.y -= 1
            self.overflowY += 1

    def down(self, num):
        self.overflowY += num
        if self.overflowY > 1:
            self.rect.y += 1
            self.overflowY -= 1

    def left(self, num):
        self.overflowX -= num
        if self.overflowX < 0:
            self.rect.x -= 1
            self.overflowX += 1

    def right(self, num):
        self.overflowX += num
        if self.overflowX > 1:
            self.rect.x += 1
            self.overflowX -= 1
