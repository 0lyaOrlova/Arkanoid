import pygame
from random import randrange


pygame.font.init()
img = pygame.image.load('data\поле.png')
pygame.display.set_icon(img)


pygame.init()
width, height = 975, 721
size = width, height
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60


x = 513
n = randrange(5, 400)
c = 5

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

#class AnimatedMissle(pygame.sprite.Sprite):
#    def __init__(self, filename):
#        super().__init__()
#        self.images = filename
#        self.index = 0
# #       self.image = self.images[self.index]
#        self.index += 1
#        if self.index >= len(self.images):
#            self.index = 0
#        self.image = self.images[self.index]

speed = 1
mirror = Game(513 // 2, 'data/зеркало.png')
missle = Missle(randrange(40, 800), 'data/Снаряд1.png')
#a_m = AnimatedMissle('Анимация_1')
a = []

if __name__ == '__main__':
    running = True
    screen.blit(bg, (0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (1, n), 5)
    pygame.draw.circle(screen, (255, 255, 255), (1, n), 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                    pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    if pressed[0]:
                        mirror.rect.x = pos[0]
        screen.blit(bg, (0, 0))
        missle.rect.y += speed
        if (missle.rect.x) < abs(c) and  (missle.rect.x + 70) > abs(c) and (missle.rect.y) < n and (missle.rect.y + 70) > n:
           # missle = a_m
            print("winner") # Показатель того, что снаряд поражен, в дальнейшем здесь будет анимация поражения снаряда
            #missle.kill()
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


