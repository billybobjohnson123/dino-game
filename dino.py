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
        self.additive_velocity= -jump_velocity
        self.num_called = 0

        self.standing_image = pygame.image.load('img/dino.png')
        self.standing_image = pygame.transform.scale(self.standing_image, (100, 100))
        
        self.walking_image1 = pygame.image.load('img/dino1.png')
        self.walking_image1 = pygame.transform.scale(self.walking_image1, (100, 100))
        self.walking_image2 = pygame.image.load('img/dino2.png')
        self.walking_image2 = pygame.transform.scale(self.walking_image2, (100, 100))
       
        self.crouched_image1 = pygame.image.load('img/dino_crouching2.png')
        self.crouched_image1 = pygame.transform.scale(self.crouched_image1, (100, 80))
        self.crouched_image2 = pygame.image.load('img/dino_crouching2.png')
        self.crouched_image2 = pygame.transform.scale(self.crouched_image2, (100, 80))

        self.current = self.walking_image1
        # self.rect = self.current.get_rect(topleft=(self.x, self.y))

        # I want to create a rectangle with height self.dino_height where the image is
        self.rect = pygame.Rect(self.x, self.y, self.dino_height, self.dino_height)
        self.crouched = False

        self.y_velocity = 0

        self.gravity = 900

    def draw(self, screen):
        if not self.crouched:
            screen.blit(self.current, self.rect)
            
        else:
            self.img_rect = pygame.Rect(self.rect.left, self.rect.top - (self.crouch_height-20), self.rect.width, self.rect.height)
            screen.blit(self.current, self.img_rect)

    def crouch(self):
        self.crouched = True
        # I want to set self.rect to have a height of self.crouch_height
        self.rect.height = self.crouch_height

    def uncrouch(self):
        self.crouched = False
        self.rect.height = self.dino_height
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
            self.additive_velocity = -self.jump_velocity

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
            return self.rect.y + self.crouch_height
        else:
            return self.rect.y + self.dino_height
        
    def set_bottom_left_y(self, val):
        if self.crouched:
            self.rect.y = val - self.crouch_height
        else:
            self.rect.y = val - self.dino_height

    def add_velocity(self): 
        self.num_called += 1
        if self.num_called >= 4:
            self.y_velocity += self.additive_velocity
            self.additive_velocity += 400
            self.additive_velocity = min(self.additive_velocity,0)
            self.num_called = 0