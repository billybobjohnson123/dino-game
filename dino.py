# Attributes: color, jump height, crouch height, dino height
# Actions: jump, crouch

#make crouch work
#get crouch 1 png back
#how transform work
#more variables clearer


import pygame

dt = 0

class Dino:
    def __init__(self,color,jump_velocity,crouch_height,dino_height, floor_y, x, y):

        self.color = color

        self.x = x
        self.y = y

        self.jump_velocity = jump_velocity
        self.crouch_height =crouch_height
        self.dino_height = dino_height
        self.current_height = dino_height
        self.floor_y = floor_y

        self.standing_image = pygame.image.load('img/dino.png')
        self.standing_image = pygame.transform.scale(self.standing_image, (100, 100))
        
        self.walking_image1 = pygame.image.load('img/dino1.png')
        self.walking_image1 = pygame.transform.scale(self.walking_image1, (100, 100))
        self.walking_image2 = pygame.image.load('img/dino2.png')
        self.walking_image2 = pygame.transform.scale(self.walking_image2, (100, 100))
       
        self.crouched_image1 = pygame.image.load('img/dino_crouching2.png')
        self.crouched_image1 = pygame.transform.scale(self.crouched_image1, (100, 100))
        self.crouched_image2 = pygame.image.load('img/dino_crouching2.png')
        self.crouched_image2 = pygame.transform.scale(self.crouched_image2, (100, 100))

        self.current = self.walking_image1
        self.rect = self.current.get_rect(topleft=(self.x, self.y))

        self.crouched = False

        self.y_velocity = 0

        self.gravity = 4000

    def draw(self, screen):
        screen.blit(self.current, self.rect)

    def crouch(self):
        self.crouched = True

    def uncrouch(self):
        self.crouched = False

    def jump(self):
        self.y_velocity = -self.jump_velocity

    def simulate(self, dt):
        if self.y_velocity != 0:
            self.rect.y += self.y_velocity * dt
            self.y_velocity += self.gravity * dt
    
        if self.get_bottom_left_y() < self.floor_y:
            self.rect.y += self.y_velocity * dt
            self.y_velocity += self.gravity * dt
        else:
            self.set_bottom_left_y(self.floor_y)
            self.y_velocity = 0

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

    def get_bottom_left_y(self):
        return self.rect.y + self.dino_height
        
    def set_bottom_left_y(self, val):
        self.rect.y = val - self.dino_height

