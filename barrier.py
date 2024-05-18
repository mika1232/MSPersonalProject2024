import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('paddle.png')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
        self.rect.x -= 100
        self.permit = True
        self.origin = [self.rect.x, self.rect.y]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, x, y):
        if self.permit:
            self.rect.midtop = [x, y]

    def originate(self):
        self.rect.x = self.origin[0]
        self.rect.y = self.origin[1]

class Barrier2(Barrier):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('paddle.png')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
        self.rect.x += 100
        self.speed = 20
        self.origin = [self.rect.x, self.rect.y]
        self.target = 0

    def reach(self, y):
        self.target = (self.rect.y-50) - y
        if abs(self.target) > 100:
            self.speed = 10
        if abs(self.target) > 200:
            self.speed = 15
        if abs(self.target) > 300:
            self.speed = 20

    def move(self):
        if self.target > 0:
            self.rect.y -= self.speed
            self.target -= self.speed
            if self.target <= 0:
                self.target = 0
        if self.target < 0:
            self.rect.y += self.speed
            self.target += self.speed
            if self.target >= 0:
                self.target = 0


