from pygame import *
from random import randint
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,  player_speed):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < w - 85:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < w - 85:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score
        if self.rect.y > h:
            self.rect.y = -50
            self.rect.x = randint(20, w-100)
            score = score + 1


w, h = 700, 500
mw = display.set_mode((w, h))
display.set_caption("Shooter")
background = transform.scale(image.load('background.png'), (w, h))

mixer.init()
mixer.music.load("background.mp3")
mixer.music.play()
fire_sound = mixer.Sound("sound.mp3")


font.init()
text1 = font.Font(None, 36)
text2 = font.Font(None, 80)


player1 = Player("player1.png", 10, 200, 30, 100, 10)
player2 = Player("player2.png", w-40, 200, 30, 100, 10)
ball = Enemy("ball.png", 200, 200, 50, 50, 10)
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    mw.blit(background, (0, 0))
    player1.reset()
    player2.reset()
    player1.update_l()
    player2.update_r()
    ball.reset()

    display.update()
    clock.tick(30)
