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
y = randrange(5, 400)
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

speed = 1
mirror = Game(513 // 2, 'data/зеркало.png')
missle = Missle(randrange(40, 800), 'data/Снаряд1.png')
a = []

if __name__ == '__main__':
    running = True
    screen.blit(bg, (0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (1, y), 5)
    pygame.draw.circle(screen, (255, 255, 255), (1, y), 2)
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
        if (missle.rect.x - 20) < c and  (missle.rect.x + 20) > c and (missle.rect.y - 20) < y and (missle.rect.y + 20) > y:
            print("winner") # Показатель того, что снаряд поражен, в дальнейшем здесь будет анимация поражения снаряда
        if y >= 715:
            c = 5
            y = randrange(5, 400)
        if (mirror.rect.x - 30) < c and  (mirror.rect.x + 30) > c and (mirror.rect.y - 20) < y and (mirror.rect.y + 20) > y:
            a.append(1)
        if y <= 5:
            a.append(2)
        if c >= 970:
            a.append(0)
        if len(a) > 0:
            if a[-1] == 1:
                c += 3
                y -= 3
            elif a[-1] == 0:
                c -= 3
                y += 3
            elif a[-1] == 2:
                c += 3
                y += 3
        else:
            y += 3
            c += 3
        pygame.draw.circle(screen, (0, 255, 0), (c, y), 5)
        pygame.draw.circle(screen, (255, 255, 255), (c, y), 2)
        screen.blit(mirror.image, mirror.rect)
        screen.blit(missle.image, missle.rect)
        pygame.display.update()
        clock.tick(FPS)


