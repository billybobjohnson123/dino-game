# Attributes: color, jump height, crouch height, dino height
# Actions: jump, crouch

#make crouch work
#get crouch 1 png back
#how transform work
#more variables clearer


import pygame

dt = 0

class Dino:
    def __init__(self,color,jump_velocity,crouch_height,dino_height, x, y):

        self.color = color

        self.x = x
        self.y = y

        self.jump_velocity = jump_velocity
        self.crouch_height =crouch_height
        print(self.crouch_height)
        self.dino_height = dino_height
        self.current_height = dino_height

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
        self.rect = self.current.get_rect(topleft=(self.x, self.y))

    def uncrouch(self):
        self.crouched = False
        self.rect = self.current.get_rect(topleft=(self.x, self.y))

    def jump(self):
        self.y_velocity = -self.jump_velocity

    def simulate(self, dt):
        self.y += self.y_velocity * dt
        self.y_velocity += self.gravity * dt

        if self.get_bottom_left_y() > 310:
            self.set_bottom_left_y(310)

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
        if self.crouched:
            return self.rect.y + 100
        else:
            return self.rect.y + 50 
        
    def set_bottom_left_y(self, val):
        if self.crouched:
            self.y = val + 50
        else:
            self.y = val + 100
