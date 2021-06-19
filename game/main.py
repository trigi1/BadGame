import pygame
import math
from bullet import Bullet
from player import Player
from enemy import Enemy

pygame.init()
screen_size = (800, 600)
bgcolor = (99, 99, 99)
screen = pygame.display.set_mode(screen_size)

realX = 0
realY = 0
mousePos = (0, 0)
xDiff = 0
yDiff = 0
diagonal = 0

pygame.display.set_caption("Test Game")
playerImg = pygame.image.load('images/icon.png')
enemyImg = pygame.image.load('images/enemy.png')
bulletImg = pygame.image.load('images/bullet.png')
pygame.display.set_icon(playerImg)

player = Player(playerImg)
bullet_group = pygame.sprite.Group()
bullet = Bullet(bulletImg, 370, -100, 0, 0)
bulletX = 0
bulletY = 0
firing = False

enemy1 = Enemy(enemyImg)
enemy2 = Enemy(enemyImg)
enemy3 = Enemy(enemyImg)
enemies = pygame.sprite.Group(enemy1, enemy2, enemy3)
movingUp = False
movingDown = False
movingLeft = False
movingRight = False

go1 = True
go2 = True
go3 = True
frame = 0

def thing(img, x, y):
    screen.blit(img, (x, y))


running = True
while running:
    frame += 1
    screen.fill(bgcolor)
    realX = player.rect.x + 16
    realY = player.rect.y + 16
    mousePos = pygame.mouse.get_pos()
    xDiff = (math.fabs(mousePos[0] - realX)) ** 2
    yDiff = (math.fabs(mousePos[1] - realY)) ** 2
    diagonal = xDiff + yDiff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movingUp = True
            elif event.key == pygame.K_s:
                movingDown = True
            elif event.key == pygame.K_a:
                movingLeft = True
            elif event.key == pygame.K_d:
                movingRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movingUp = False
            elif event.key == pygame.K_s:
                movingDown = False
            elif event.key == pygame.K_a:
                movingLeft = False
            elif event.key == pygame.K_d:
                movingRight = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if math.fabs(diagonal) > 0.001:
                    bulletX = math.sqrt(xDiff / diagonal) * 0.23
                    bulletY = math.sqrt(yDiff / diagonal) * 0.23
                    if realX > mousePos[0]:
                        bulletX = -bulletX
                    if realY > mousePos[1]:
                        bulletY = -bulletY
                else:
                    bulletX = 0
                    bulletY = 0.23
                bullet_group.add(player.create_bullet(bulletImg, player.rect.x + 12, player.rect.y - 8, bulletX, bulletY))
    if movingUp:
        player.up(0.2)
    if movingDown:
        player.down(0.2)
    if movingRight:
        player.right(0.2)
    if movingLeft:
        player.left(0.2)
    if player.rect.x < 0:
        player.rect.x = 0
    elif player.rect.x > 768:
        player.rect.x = 768
    if pygame.sprite.spritecollideany(player, enemies):
        print("cringe you lost")
        running = False
    col_list = pygame.sprite.groupcollide(bullet_group, enemies, False, False)
    for key, value in col_list.items():
        for i in value:
            i.hp -= 1
            if i.hp <= 0:
                i.kill()
        key.kill()
    if player.rect.y < 0:
        player.rect.y = 0
    elif player.rect.y > 568:
        player.rect.y = 568
    for i in enemies:
        if i.rect.x < player.rect.x:
            i.right()
        else:
            i.left()
        if i.rect.y < player.rect.y:
            i.down()
        else:
            i.up()
    bullet_group.update()
    if bullet.rect.y <= 0 or bullet.rect.y >= 592 or bullet.rect.x <= 0 or bullet.rect.x >= 792:
        bullet.rect.y = -100
        firing = False
    if (not go1) and (not go2) and (not go3):
        print("yay you won!")
        running = False
    thing(playerImg, player.rect.x, player.rect.y)
    for i in enemies:
        thing(enemyImg, i.rect.x, i.rect.y)
    thing(bulletImg, bullet.rect.x, bullet.rect.y)
    bullet_group.draw(screen)
    pygame.display.update()
