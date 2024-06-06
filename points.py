import pygame


class Point_Display(pygame.sprite.Sprite):
    def __init__(self, text, text2):
        super().__init__()
        self.scoring_system = [0, 10, 15, 30, 45, "END OF GAME"]
        self.text2 = text2
        self.text = text
        self.font = pygame.font.Font(r"mainfont.ttf", 40)
        self.image = self.font.render(f"SCORE: {text}", True, (255, 0, 0))
        self.image2 = self.font.render(f"SCORE: {text2}", True, (0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()

        surf = pygame.display.get_surface()

        self.rect.topleft = surf.get_rect().topleft
        self.rect2.topright = surf.get_rect().topright

    def draw(self, surface, t1, t2):
        if t1 < 6 and t2 < 6:
            self.image = self.font.render(f"SCORE: {self.scoring_system[int(t1)]}", True, (0, 255, 0))
            self.image2 = self.font.render(f"SCORE: {self.scoring_system[int(t2)]}", True, (0, 0, 255))
            surface.blit(self.image, self.rect)
            surface.blit(self.image2, self.rect2)
            self.image = self.font.render(f"SCORE: {self.scoring_system[int(t1)]}", True, (0, 255, 0))
            self.image2 = self.font.render(f"SCORE: {self.scoring_system[int(t2)]}", True, (0, 0, 255))
            self.rect = self.image.get_rect()
            self.rect2 = self.image2.get_rect()
            surf = pygame.display.get_surface()

            self.rect.topleft = surf.get_rect().topleft
            self.rect2.topright = surf.get_rect().topright


