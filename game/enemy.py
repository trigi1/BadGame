import pygame
import random
from bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 768)
        self.rect.y = 50
        self.overflowX = 0
        self.overflowY = 0
        self.hp = 3

    def up(self):
        self.overflowY -= 0.15
        if self.overflowY < 0:
            self.rect.y -= 1
            self.overflowY += 1

    def down(self):
        self.overflowY += 0.15
        if self.overflowY > 1:
            self.rect.y += 1
            self.overflowY -= 1

    def left(self):
        self.overflowX -= 0.15
        if self.overflowX < 0:
            self.rect.x -= 1
            self.overflowX += 1

    def right(self):
        self.overflowX += 0.15
        if self.overflowX > 1:
            self.rect.x += 1
            self.overflowX -= 1

    def tp(self, xpos, ypos):
        self.rect.x = xpos
        self.rect.y = ypos

    def create_enemy_bullet(self, img, x, y, ax, ay):
        return Bullet(img, x, y, ax, ay)
