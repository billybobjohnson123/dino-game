import pygame
import dino
import obstacles


dt = 0

pygame.init()
font = pygame.font.Font('font/PressStart2P-Regular.ttf', 32)
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

height = 500
dino = dino.Dino((0,0,0), height * 4/5, height/2, height, 200, 410)
obstacle = obstacles.Obstacle(500, 430)
pygame.display.set_icon(pygame.image.load('img/dino.png'))
pygame.display.set_caption("Dino Game")
count = 0
game_over = False


while True:
    dt = clock.tick(60) / 1000.0
    dino.simulate(dt) # wait until next frame (at 60 FPS)
    obstacle.simulate(dt)
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.mod != pygame.KMOD_NONE:
                if event.mod & (pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT):
                    dino.crouch()
        if event.type == pygame.KEYUP:
            if event.mod != pygame.KMOD_NONE:
                if event.mod & ~(pygame.KMOD_LSHIFT | pygame.KMOD_RSHIFT):
                    dino.uncrouch()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_SPACE] and dino.y > 400:
        dino.jump()

    # Do logical updates here.
    # ...

    screen.fill("white")  # Fill the display with a solid color
    dino.draw(screen)
    obstacle.draw(screen, obstacle.x, obstacle.y)

    ground = pygame.Rect((0, 500), (1280, 220))

    pygame.draw.rect(screen, (0,0,0), ground)


    pygame.draw.rect(screen, (255,0,0), dino.rect, 2)
    pygame.draw.rect(screen, (255,0,0), obstacle.rect, 2)

    print(dino.rect)


    # Render the graphics here.
    # ...
    if count > 100:
        count = 0
    if count % 5 == 0:
        dino.walk()
    
    
    count += 1

    if dino.rect.colliderect(obstacle.rect):
        game_over = True
        
    if game_over:
        screen.blit(font.render('Hello!', True, (255,0,0)), (200, 100))
        



    pygame.display.flip()  # Refresh on-screen display

