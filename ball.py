import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.center = surface.get_rect().center

        self.move = [random.choice([-10, 10, -15, 15]), random.choice([-10, 10, -15, 15])]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move[0]
        self.rect.y += self.move[1]

    def hit_wall(self, type):
        if (type%2) != 0:
            self.move[1] = self.move[1]
            self.move[0] = self.move[0]*-1
        else:
            self.move[1] = self.move[1]*-1
            self.move[0] = self.move[0]

    def teleport(self, coorx, coory):
        self.rect.x = coorx
        self.rect.y = coory

class AI_ball(Ball):
    def __init__(self, ball):
        super().__init__()
        self.move1 = [ball.move[0]*2, ball.move[1]*2]
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.move2 = ball.move
        self.move = self.move2
        self.rect.center = ball.rect.center

    def reset(self, ball):
        self.rect.center = ball.rect.center
        self.move = ball.move

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move1[0]
        self.rect.y += self.move1[1]
