import pygame


def load_image(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)


class Player:
    def __init__(self, x, y):
        self.score = 0
        self.walk_down = [
            load_image("actions/walkingjosefront.png", (50, 50)),
            load_image("actions/walkingjosefrontclose.png", (50, 50)),
        ]

        self.walk_up = [
            load_image("actions/walkingbackjoseleft.png", (50, 50)),
            load_image("actions/walkingbackjoseright.png", (50, 50)),
        ]

        self.walk_left = [
            load_image("actions/sideleftwalking.png", (50, 50)),
            load_image("actions/sideleftwalkingright.png", (50, 50)),
        ]

        self.walk_right = [
            load_image("actions/siderightwalk.png", (50, 50)),
            load_image("actions/siderightwalkleft.png", (50, 50)),
        ]

        self.images = self.walk_down
        self.frame = 0
        self.image = self.images[0]

        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 5
        self.stamina = 100
        self.max_stamina = 100

    def move(self, keys, width, height):
        moving = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.images = self.walk_left
            moving = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.images = self.walk_right
            moving = True

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.images = self.walk_up
            moving = True

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.images = self.walk_down
            moving = True

        if moving:
            self.frame += 0.2
            if self.frame >= len(self.images):
                self.frame = 0
            self.image = self.images[int(self.frame)]
            self.stamina -= 0.2

        if self.stamina <= 0:
            self.speed = 2
        else:
            self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # stamina bar
        pygame.draw.rect(screen, (255,255,255), (20,20,200,20))
        pygame.draw.rect(screen, (0,200,0),
        (20,20,int(200*(self.stamina/self.max_stamina)),20))