import pygame, random

def load(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

class PowerUp:
    def __init__(self):
        self.image = load("powerup/coins.png", (30,30))
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.x = random.randint(50,750)
        self.rect.y = random.randint(120,500)

    def draw(self, screen):
        screen.blit(self.image, self.rect)