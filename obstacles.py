#Attributes for cacti: height, width, position, graphic
#Attributes for Pterodactyl: height, width, position, graphic
import pygame

class Obstacle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.speed = 600

        self.image = pygame.image.load("img/dino_cactus.png")
        self.cactus_image = pygame.transform.scale(self.image, (50, 70))

        self.rect = self.cactus_image.get_rect(x=self.x, y=self.y)


    def simulate(self, dt):
        self.x -= self.speed * dt
        self.rect.x = self.x

    def draw(self, screen, x, y):
        screen.blit(self.cactus_image, self.rect)
