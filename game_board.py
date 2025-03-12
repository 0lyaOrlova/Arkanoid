import random

import pygame
from random import randrange, choice
from pygame.constants import K_ESCAPE, KEYDOWN


pygame.font.init()
img = pygame.image.load('data\поле.png')
pygame.display.set_icon(img)


pygame.init()
width, height = 975, 721
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 20


x = 513
n = randrange(5, 400)
c = 5
filename = random.choice(['data/Снаряд1.png', 'data/Снаряд2.png', 'data/Снаряд3.png'])

bg = pygame.image.load('data/поле.png').convert()



class Game(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 500))

class Missle(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 40))


class AnimatedMissle(pygame.sprite.Sprite):
    def __init__(self, w1, h1, k, filename, position):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.position = position
        self.k = k
        self.sprite = pygame.image.load(filename).convert_alpha()

        wi, hi = self.sprite.get_size()
        self.w, self.h = wi / w1, hi / h1


        row = 0

        for j in range(int(hi / self.h)):
            for i in range(int(wi / self.w)):
                self.frames.append(self.sprite.subsurface(pygame.Rect(i * self.w, row, self.w, self.h)))
            row += int(self.h)

speed = 1
mirror = Game(513 // 2, 'data/зеркало.png')
missle = Missle(randrange(40, 800), filename)
#a_m = AnimatedMissle(14, 1, 14, 'data/Анимация1.png', (100, 100))
a = []
counter = 0
v = []

if __name__ == '__main__':
    running = True
    screen.blit(bg, (0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (1, n), 5)
    pygame.draw.circle(screen, (255, 255, 255), (1, n), 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            elif event.type == pygame.MOUSEMOTION:
                    pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    if pressed[0]:
                        mirror.rect.x = pos[0]
        screen.blit(bg, (0, 0))
        missle.rect.x += speed
        missle.rect.y += speed
        if (missle.rect.x) < abs(c) and  (missle.rect.x + 70) > abs(c) and (missle.rect.y) < n and (missle.rect.y + 70) > n:
            v.clear()
            g = (missle.rect.x, missle.rect.y)
            v.append(g)
            v.append(filename)
            missle = Missle(randrange(40, 800), random.choice(['data/Снаряд1.png', 'data/Снаряд2.png', 'data/Снаряд3.png']))
            print(v)
        if len(v) > 0:
            if v[1] == 'data/Снаряд1.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация1.png', v[0])
            elif v[1] == 'data/Снаряд2.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация2.png', v[0])
            elif v[1] == 'data/Снаряд3.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация3.png', v[0])
            counter = (counter + 1)
            if counter >= 14:
                counter = 0
                v.clear()
            screen.blit(a_m.frames[counter], a_m.position)
        if missle.rect.x == 975 or missle.rect.y == 720:
            missle.rect.x, missle.rect.y = randrange(40, 800), 40
        #counter = (counter + 1) % a_m.k
        if n >= 716:
            n = randrange(10, 350)
            c = 5
            pygame.draw.circle(screen, (0, 255, 0), (25, n), 5)
            pygame.draw.circle(screen, (255, 255, 255), (25, n), 2)
        if (mirror.rect.x) < abs(c) and (mirror.rect.x + 80) > abs(c) and (mirror.rect.y) < n and (mirror.rect.y + 92) > n:
            a.append(1)
        if n <= 5:
            a.append(2)
        if c >= 970:
            a.append(0)
        if len(a) > 0:
            if a[-1] == 1:
                c += 3
                n -= 3
            elif a[-1] == 0:
                c -= 3
                n += 3
            elif a[-1] == 2:
                c += 3
                n += 3
        else:
            n += 3
            c += 3
        pygame.draw.circle(screen, (0, 255, 0), (abs(c), n), 5)
        pygame.draw.circle(screen, (255, 255, 255), (abs(c), n), 2)
        screen.blit(mirror.image, mirror.rect)
        screen.blit(missle.image, missle.rect)
        pygame.display.update()
        clock.tick(FPS)


