# Attributes: color, jump height, crouch height, dino height
# Actions: jump, crouch
import pygame
class Dino:
    def __init__(self,color,jump_height,crouch_height,dino_height):
        self.color = color
        self.jump_height = jump_height
        self.crouch_height =crouch_height
        self.dino_height = dino_height
        self.current_height = dino_height
        self.standing_image = pygame.image.load('img/dino.png')
        self.standing_image = pygame.transform.scale(self.standing_image, (100, 100))
        self.crouched_image = pygame.image.load('img/dino_crouching.png')
        self.crouched_image = pygame.transform.scale(self.crouched_image, (100, 100))
        self.crouched = False
    def draw(self, screen, x, y):
        if self.crouched:
            screen.blit(self.crouched_image, (x, y))
        else:
            screen.blit(self.standing_image, (x, y))
    def crouch(self):
        self.crouched = True
    def uncrouch(self):
        self.crouched = False