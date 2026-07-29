import pygame
import dino
import obstacles
import random
#fix spawning logic to spawn only a single obs at once, add some logic to prevent pteros from spawnign too early
dt = 0
frames = 0
frames2 = 0
obs = []
score = 0
floor_y = 500
screen_width = 1280
screen_height = 720
obstacle_types = ["cactus", "pterodactyl"]

pygame.init()
font = pygame.font.Font('font/PressStart2P-Regular.ttf', 32)
score_font = pygame.font.Font('font/PressStart2P-Regular.ttf', 20)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

height = 100
dino = dino.Dino((0,0,0), 700, height/2 , height, floor_y, 200, 0)
pygame.display.set_icon(pygame.image.load('img/dino.png'))
pygame.display.set_caption("Dino Game")
count = 0
game_over = False
running = False


while True:
    if not running and not game_over:
         screen.blit(font.render('PRESS SPACE TO START!', True, (255,0,0)), (300, 100)) 
         pygame.display.flip()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.mod != pygame.KMOD_NONE:
                if event.mod & (pygame.KMOD_LSHIFT or pygame.KMOD_RSHIFT):
                    dino.crouch()
        if event.type == pygame.KEYUP:
            if event.mod != pygame.KMOD_NONE:
                if event.mod & ~(pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT):
                    dino.uncrouch()

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        game_over = False
        running = True
    if not running:
        continue
    dt = clock.tick(60) / 1000.0
    frames += 1
    frames2 += 1
    score += 1
    # Process player inputs.
    dino.simulate(dt) # wait until next frame (at 60 FPS)
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_DOWN] and dino.get_bottom_left_y() == floor_y:
        dino.crouch()
    if (pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]) and dino.get_bottom_left_y() == floor_y:
        dino.jump()
    if pressed_keys[pygame.K_DOWN]:
        dino.gravity = 5000
    else:
        dino.gravity = 1200
    if frames > 80:
        num = random.randint(-150,150)
        frames = 0
        print('run')
        choice = random.choices(obstacle_types, weights=[3, 1], k=1)[0]
        if choice == "cactus":
            obstacle = obstacles.Obstacle(1280+num, floor_y, "cactus")
        else:
            obstacle = obstacles.Obstacle(1280+num, floor_y, "pterodactyl")
        obs.append(obstacle)
    for i in obs:
        i.simulate(dt)
        
    # Do logical updates here.
    # ...

    screen.fill("white")  # Fill the display with a solid color
    dino.draw(screen)
    
    for j in obs:
        j.draw(screen, j.x, j.y)

    ground = pygame.Rect((0, floor_y), (screen_width, screen_height-floor_y))

    pygame.draw.rect(screen, (0,0,0), ground)


    pygame.draw.rect(screen, (255,0,0), dino.rect, 2)
    for i in obs:
        pygame.draw.rect(screen, (255,0,0), i.rect, 2)



    # Render the graphics here.
    # ...
    if count > 100:
        count = 0
    if count % 5 == 0:
        dino.walk()
    
    
    count += 1

    for k in obs:
        if dino.rect.colliderect(k.rect):
            game_over = True
        
    if game_over:
        screen.blit(font.render('GAME OVER!', True, (255,0,0)), (500, 100))
        running = False
    
    screen.blit(score_font.render(str(score), True, (128,128,128)), (1100, 100))

    pygame.display.flip()  # Refresh on-screen display()

