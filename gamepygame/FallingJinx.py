import pygame
import random

CELL_SIZE = 50


def load(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)


class FallingJinx:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.images = [
            load("powerupandpoeple/decreasetime1.png", (50, 50)),
            load("powerupandpoeple/decreasetime2.png", (50, 50))
        ]

        self.frame = 0
        self.animation_speed = 0.18

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.active = False

        self.speed = 10

        self.spawn_timer = 0
        self.spawn_delay = 120

    def spawn(self, player):

        self.rect = self.image.get_rect()

        self.rect.centerx = player.image_rect.centerx

        self.rect.y = -60

        self.speed = random.randint(9, 13)

        self.active = True

    def update(self, player):

        self.spawn_timer += 1

        if not self.active:

            if self.spawn_timer >= self.spawn_delay:

                self.spawn(player)

                self.spawn_timer = 0

            return

        self.frame += self.animation_speed

        if self.frame >= len(self.images):
            self.frame = 0

        old_center = self.rect.center

        self.image = self.images[int(self.frame)]

        self.rect = self.image.get_rect(center=old_center)

        self.rect.y += self.speed

        if self.rect.top > self.height:
            self.active = False

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, self.rect)
