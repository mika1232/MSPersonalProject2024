import pygame


class Menu_Text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Menu PIP.png")
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center

    def draw(self, surface):
        surface.blit(self.image, self.rect)


