import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, ax, ay):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.overflowX = 0
        self.overflowY = 0
        self.amountY = ay
        self.amountX = ax

    def move_y(self, num):
        self.overflowY += num
        if self.overflowY < 0:
            self.rect.y -= 1
            self.overflowY += 1
        if self.overflowY > 1:
            self.rect.y += 1
            self.overflowY -= 1

    def move_x(self, num):
        self.overflowX += num
        if self.overflowX < 0:
            self.rect.x -= 1
            self.overflowX += 1
        if self.overflowX > 1:
            self.rect.x += 1
            self.overflowX -= 1

    def tp(self, xpos, ypos):
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):
        self.overflowY += self.amountY
        if self.overflowY < 0:
            self.rect.y -= 1
            self.overflowY += 1
        if self.overflowY > 1:
            self.rect.y += 1
            self.overflowY -= 1
        self.overflowX += self.amountX
        if self.overflowX < 0:
            self.rect.x -= 1
            self.overflowX += 1
        if self.overflowX > 1:
            self.rect.x += 1
            self.overflowX -= 1
