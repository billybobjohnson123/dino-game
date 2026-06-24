# Attributes: color, jump height, crouch height, dino height
# Actions: jump, crouch
import pygame

dt = 0

class Dino:
    def __init__(self,color,jump_height,crouch_height,dino_height, x, y):

        self.color = color

        self.x = x
        self.y = y

        self.jump_height = jump_height
        self.crouch_height =crouch_height
        self.dino_height = dino_height
        self.current_height = dino_height

        self.standing_image = pygame.image.load('img/dino.png')
        self.standing_image = pygame.transform.scale(self.standing_image, (100, 100))
        
        self.walking_image1 = pygame.image.load('img/dino1.png')
        self.walking_image1 = pygame.transform.scale(self.walking_image1, (100, 100))
        self.walking_image2 = pygame.image.load('img/dino2.png')
        self.walking_image2 = pygame.transform.scale(self.walking_image2, (100, 100))
       
        self.crouched_image1 = pygame.image.load('img/dino_crouching1.png')
        self.crouched_image1 = pygame.transform.scale(self.crouched_image1, (100, 100))
        self.crouched_image2 = pygame.image.load('img/dino_crouching2.png')
        self.crouched_image2 = pygame.transform.scale(self.crouched_image2, (100, 100))



        self.current = self.walking_image1
        self.rect = self.current.get_rect(x = self.x, y = self.y)


        self.crouched = False

        self.y_velocity = 0

        self.gravity = 600

    def draw(self, screen):
        screen.blit(self.current, self.rect)

    def crouch(self):
        self.crouched = True
        self.rect = self.current.get_rect(x = self.x, y = self.y)

    def uncrouch(self):
        self.crouched = False
        self.rect = self.current.get_rect(x = self.x, y = self.y)

    def jump(self):
        
        self.y_velocity = -self.jump_height

    def simulate(self, dt):
        self.y += self.y_velocity * dt
        self.y_velocity += self.gravity * dt

        if self.y > 410:
            self.y = 410

        self.rect.y = self.y

    def walk(self):

        if self.crouched:
            if self.current == self.crouched_image1:
                self.current = self.crouched_image2
            else:
                self.current = self.crouched_image1

        else: 
            if self.current == self.walking_image1:
                self.current = self.walking_image2
            else:
                self.current = self.walking_image1