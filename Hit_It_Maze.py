import pygame
from pygame import *
import math as m
pygame.init()
pygame.font.init()

back = (252, 255, 204)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
jam = pygame.time.Clock()

chaser_speed = 1.5

font_color1 = (0,255,0)
font_color2 = (255, 0, 0)
font = font.Font(None,35)
win = font.render("YOU WON",True, font_color1)
lose = font.render("YOU LOST",True, font_color2)

class Wall():
    def __init__(self,x,y,width,height,color):
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(mw, self.color, self.rect)
        
    def crash(self, player):
        return self.rect.colliderect(player)

class Character(pygame.sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gerak = None

    def show(self):
        mw.blit(self.image  , (self.rect.x, self.rect.y))

    def crash(self, rect):
        return self.rect.colliderect(rect)

class Player(Character):
    def control(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < 500:
            self.rect.x += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Enemy(Character):
    def guard(self, pos_1, pos_2):
        if self.rect.y > pos_1:
            self.gerak = "up"

        if self.rect.y < pos_2:
            self.gerak = "down"

        if self.gerak == 'down':
            self.rect.y += self.speed
        else: 
            self.rect.y -= self.speed

    def chase(self, target, speed):
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y

        distance = m.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
            self.rect.x += dx * speed
            self.rect.y += dy * speed

class Target():
    def __init__(self, x, y, width, height, first_col, second_col):
        self.rect = pygame.Rect(x, y, width, height)
        self.first_col = first_col
        self.second_col = second_col

    def draw(self):
        pygame.draw.rect(mw, self.first_col, self.rect)
        pygame.draw.rect(mw, self.second_col, self.rect, 5)
        
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

turtle = Player('Turtle-removebg-preview.png', 50, 450, 30, 30, 5)
guardian1 = Enemy('Guardian_Rabbit-removebg-preview.png', 350, 150, 30, 30, 2)
guardian2 = Enemy('Guardian_Rabbit-removebg-preview.png', 350, 350, 30, 30, 2)
chaser = Enemy('Chasing_Rabbit-removebg-preview.png', 130, 325, 70, 70, chaser_speed)

target1 = Target(450, 160, 20, 20, WHITE, GREEN)
target2 = Target(20, 15, 20, 20, WHITE, YELLOW)
target3 = Target(450, 450, 20, 20, WHITE, RED)

wall_1 = Wall(0, 0, 500, 10, BLACK)
wall_2 = Wall(490, 0, 10, 500, BLACK)
wall_3 = Wall(0, 490, 500, 10, BLACK)
wall_4 = Wall(0, 0, 10, 500, BLACK)
wall_5 = Wall(220, 0, 10, 150, BLACK)
wall_6 = Wall(350, 130, 150, 10, BLACK)
wall_7 = Wall(270, 350, 10, 150, BLACK)
wall_8 = Wall(80, 50, 10, 150, BLACK)
wall_9 = Wall(150, 150, 10, 150, BLACK)
wall_10 = Wall(100, 300, 110, 10, BLACK)
wall_11 = Wall(300, 50, 150, 10, BLACK)
wall_12 = Wall(360, 400, 70, 10, BLACK)
wall_13 = Wall(430, 400, 10, 90, BLACK)
wall_14 = Wall(350, 225, 150, 10, BLACK)
wall_15 = Wall(350, 225, 10, 70, BLACK)
wall_16 = Wall(0, 415, 200, 10, BLACK)
wall_17 = Wall(200, 360, 10, 65, BLACK)

targets = list()
targets.append(target1)
targets.append(target2)
targets.append(target3)

game_start = True
while game_start:
    mw.fill(back)
    turtle.show()
    guardian1.show()
    guardian2.show()
    chaser.show()
    wall_1.draw()
    wall_2.draw()
    wall_3.draw()
    wall_4.draw()
    wall_5.draw()
    wall_6.draw()
    wall_7.draw()
    wall_8.draw()
    wall_9.draw()
    wall_10.draw()
    wall_11.draw()
    wall_12.draw()
    wall_13.draw()
    wall_14.draw()
    wall_15.draw()
    wall_16.draw()
    wall_17.draw()

    turtle.control()
    guardian1.guard(195, 140)
    guardian2.guard(370, 290)
    chaser.chase(turtle, chaser_speed)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_start = False

    if wall_1.crash(turtle) or wall_2.crash(turtle) or wall_3.crash(turtle) or wall_4.crash(turtle) or wall_5.crash(turtle) or wall_6.crash(turtle) or wall_7.crash(turtle) or wall_8.crash(turtle) or wall_9.crash(turtle) or wall_10.crash(turtle) or wall_11.crash(turtle) or wall_12.crash(turtle) or wall_13.crash(turtle) or wall_14.crash(turtle) or wall_15.crash(turtle) or wall_16.crash(turtle) or wall_17.crash(turtle):
        turtle.rect.x, turtle.rect.y = 50, 425

    if sprite.collide_rect(turtle, guardian1) or sprite.collide_rect(turtle, guardian2) or sprite.collide_rect(turtle, chaser):
        turtle.speed = 0
        guardian1.speed = 0
        guardian2.speed = 0
        chaser_speed = 0
        mw.blit(lose, (200, 250))

    for t in targets:
        t.draw()
        if sprite.collide_rect(turtle, t):
            targets.remove(t)
            t.draw()

    if len(targets) == 0:
        turtle.speed = 0
        guardian1.speed = 0
        guardian2.speed = 0
        chaser_speed = 0
        mw.blit(win, (205, 250))

    pygame.display.update()
    jam.tick(40)