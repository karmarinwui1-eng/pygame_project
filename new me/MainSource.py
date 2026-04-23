import pygame
import sys

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 410


SCREEN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption("Late-uli")

BackGround = pygame.image.load('bg.jpg')
BackGround = pygame.transform.scale(BackGround, (SCREEN_WIDHT, SCREEN_HEIGHT))

new_icon = pygame.image.load('logo1.png')
new_icon = pygame.transform.scale(new_icon, (32, 32))
pygame.display.set_icon(new_icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.blit(BackGround, (0,0))
    pygame.display.update()

pygame.quit()
sys.exit()

#our game needs is, menu buttons then, yung game, character  event, collision


