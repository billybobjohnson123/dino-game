#Attributes for cacti: height, width, position, graphic
#Attributes for Pterodactyl: height, width, position, graphic
import pygame
import random

class Obstacle:

    def __init__(self, x, floor, type, speed):

        self.x = x
        self.floor = floor

        self.size = random.randint(50, 90)
        self.speed = speed

        self.cactus_image = pygame.image.load("img/dino_cactus.png")
        self.cactus_image = pygame.transform.scale(self.cactus_image, (self.size, self.size))
        self.pterodactyl_image = pygame.image.load("img/pterodactyl1.png")
        self.pterodactyl_image = pygame.transform.scale(self.pterodactyl_image, (self.size*1.5, self.size))
        if type == "cactus":
            self.image = self.cactus_image
            self.y = floor - self.size
        else:
            self.image = self.pterodactyl_image
            self.y = floor - self.size*2
        self.rect = self.image.get_rect(x=self.x, y=self.y)


    def simulate(self, dt):
        self.x -= self.speed * dt
        self.rect.x = self.x

    def draw(self, screen, x, y):
        screen.blit(self.image, self.rect)