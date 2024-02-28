import pygame


class Menu_Text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(r"mainfont.ttf", 40)
        self.image = self.font.render(f"To play with AI raise one finger", True, (255, 0, 0))
        self.image2 = self.font.render(f"To play with a friend raise two fingers", True, (0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()

        surf = pygame.display.get_surface()

        self.rect.midtop = surf.get_rect().midtop
        self.rect.y += 60

        self.rect2.midtop = self.rect.midtop
        self.rect2.y += 60

    def draw(self, surface):
        self.image = self.font.render(f"To play with AI raise one finger", True, (255, 0, 0))
        self.image2 = self.font.render(f"To play with a friend raise two fingers", True, (0, 0, 255))
        surface.blit(self.image, self.rect)
        surface.blit(self.image2, self.rect2)
        self.image = self.font.render(f"To play with AI raise one finger", True, (255, 0, 0))
        self.image2 = self.font.render(f"To play with a friend raise two fingers", True, (0, 0, 255))
        surf = pygame.display.get_surface()

        self.rect.midtop = surf.get_rect().midtop
        self.rect.y += 60

        self.rect2.midtop = self.rect.midtop
        self.rect2.y += 60


