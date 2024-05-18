import pygame
import cv2

from PIL import Image
class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ''
    def draw(self, screen):
        image = pygame.image.load("cur_image.png")
        rect = image.get_rect()
        surface = pygame.display.get_surface()
        rect.center = surface.get_rect().center
        screen.blit(image, rect)