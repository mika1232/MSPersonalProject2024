import pygame

class Border(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('barrier.png')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center


    def draw(self, screen):
        for x in self.rect:
            screen.blit(self.image, self.rect)

class Top_Border(Border):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('barr2.png')
        self.rect.topleft = pygame.display.get_surface().get_rect().topleft

