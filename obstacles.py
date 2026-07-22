#Attributes for cacti: height, width, position, graphic
#Attributes for Pterodactyl: height, width, position, graphic
import pygame

class Obstacle:

    def __init__(self, x, y, type):

        self.x = x
        self.y = y

        self.speed = 500

        self.cactus_image = pygame.image.load("img/dino_cactus.png")
        self.cactus_image = pygame.transform.scale(self.cactus_image, (50, 70))
        self.pterodactyl_image = pygame.image.load("img/pterodactyl1.png")
        self.pterodactyl_image = pygame.transform.scale(self.pterodactyl_image, (90, 60))
        if type == "cactus":
             self.image = self.cactus_image
        else:
             self.image = self.pterodactyl_image

        self.rect = self.image.get_rect(x=self.x, y=self.y)


    def simulate(self, dt):
        self.x -= self.speed * dt
        self.rect.x = self.x

    def draw(self, screen, x, y):
            screen.blit(self.image, self.rect)
