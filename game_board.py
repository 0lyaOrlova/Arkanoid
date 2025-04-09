import pygame
from random import randrange, choice
import os
import sys
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
k = 1
filename = choice(['data/Снаряд1.png', 'data/Снаряд2.png', 'data/Снаряд3.png'])
pygame.display.set_caption("Заставка")
pygame.display.set_caption("Правилa")
bg = pygame.image.load('data/поле.png').convert()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображениями '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ДОБРО ПОЖАЛОВАТЬ!",
                  "Нажмите на экран для продолжения"]
    fon = pygame.transform.scale(load_image('Заставка.png'), ((width, height)))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 100

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return pravila_screen

        pygame.display.flip()

def pravila_screen():
    intro_text = ["Существует планета,  которую нужно 'защищать' от снарядов",
                  "Для этого на орбите запускается лазер(на данный момент изображён зелёным шариком),",
                  "его необходимо отражать с помощью зеркал(платформа, правая, левая и верхняя грани экрана).",
                  "За поражение каждого снаряда начисляется некоторое количество очков.",
         "Когда игрок набирает определённое число очков, скорость движения снарядов увеличивается."
                  ]
    fon = pygame.transform.scale(load_image('Правилa.png'), ((width, height)))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 100

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return mirror

        pygame.display.flip()

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
    start_screen()
    pravila_screen()
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
            filename = choice(['data/Снаряд1.png', 'data/Снаряд2.png', 'data/Снаряд3.png'])
            missle = Missle(randrange(40, 800), filename)
        if len(v) > 0:
            if v[1] == 'data/Снаряд1.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация1.png', v[0])
                k += 5
            elif v[1] == 'data/Снаряд2.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация2.png', v[0])
                k += 10
            elif v[1] == 'data/Снаряд3.png':
                a_m = AnimatedMissle(14, 1, 14, 'data/Анимация3.png', v[0])
                k += 15
            counter = (counter + 1)
            if counter >= 14:
                counter = 0
                v.clear()
            screen.blit(a_m.frames[counter], a_m.position)
        if missle.rect.x == 975 or missle.rect.y == 720:
            missle.rect.x, missle.rect.y = randrange(40, 800), 40
        if n >= 716:
            n = randrange(10, 350)
            c = 5
            pygame.draw.circle(screen, (0, 255, 0), (25, n), 5)
            pygame.draw.circle(screen, (255, 255, 255), (25, n), 2)
        if (mirror.rect.x) < abs(c) and (mirror.rect.x + 80) > abs(c) and (mirror.rect.y) < n and (
                mirror.rect.y + 92) > n:
            if len(a) == 0:
                a.append(1)
            elif a[-1] == 2 and (a[-2] == 3):
                a.append(1)
            else:
                a.append(3)
        if n <= 10:
            a.append(2)
        if c >= 970:
            a.append(0)
        if len(a) > 0:
            if a[-1] == 1:
                c = abs(c) + 3
                n -= 3
            elif a[-1] == 0 and a[-2] == 2:
                c -= 3
                n += 3
            elif a[-1] == 0 and a[-2] == 1:
                c -= 3
                n -= 3
            elif a[-1] == 2 and a[-2] != 0:
                if a[-2] == 3:
                    c -= 3
                    n += 3
                elif a[-2] == 1:
                    c += 3
                    n += 3
            elif a[-1] == 2 and a[-2] == 0:
                c -= 3
                n += 3
            elif a[-1] == 3:
                c -= 3
                n -= 3
        else:
            n += 3
            c += 3
        if k % 31 == 0:
            FPS += 10
        pygame.draw.circle(screen, (0, 255, 0), (abs(c), n), 5)
        pygame.draw.circle(screen, (255, 255, 255), (abs(c), n), 2)
        screen.blit(mirror.image, mirror.rect)
        screen.blit(missle.image, missle.rect)
        pygame.display.update()
        clock.tick(FPS)


