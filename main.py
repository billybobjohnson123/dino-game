import pygame
import dino
import obstacles

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

height = 500
dino = dino.Dino((0,0,0), height * 2/3, height/2, height)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color
    dino.crouch()
    dino.draw(screen, 200, 200)
    # Render the graphics here.
    # ...
    dino.uncrouch()
    dino.draw(screen, 600, 200)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)