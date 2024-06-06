import pygame
import cv2

from PIL import Image
class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ''
        self.mode = 0
        self.won = 0
    def draw(self, screen):
        if self.mode == 0:
            image = pygame.image.load("cur_image.png")
        else:
            if self.won == 1:
                image = pygame.image.load("Player1.png")
            else:
                image = pygame.image.load("Player2.png")
        rect = image.get_rect()
        surface = pygame.display.get_surface()
        rect.center = surface.get_rect().center
        screen.blit(image, rect)