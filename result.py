import pygame
import cv2

from PIL import Image
class Result(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ''
    def draw(self, screen, f):
        if f == 1:
            image = pygame.image.load("Player1.png")
        else:
            image = pygame.image.load("Player2.png")
        rect = image.get_rect()
        surface = pygame.display.get_surface()
        rect.center = surface.get_rect().center
        screen.blit(image, rect)