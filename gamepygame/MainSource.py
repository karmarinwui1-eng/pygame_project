import pygame
import sys

from Player import Player
from Vehicle import create_vehicles
from PowerUp import PowerUp
from Menu import Menu

pygame.init()

# =========================
# SETTINGS
# =========================
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Late-Uli")

clock = pygame.time.Clock()

# =========================
# LOAD BACKGROUND
# =========================
road_img = pygame.image.load("roads/cross.png").convert()
road_img = pygame.transform.smoothscale(road_img, (WIDTH, HEIGHT))

# =========================
# MENU INSTANCE
# =========================
menu = Menu(screen, WIDTH, HEIGHT)

# =========================
# GAME FUNCTION
# =========================
def game():
    player = Player(WIDTH // 2, HEIGHT - 60)

    level = 1
    vehicles = create_vehicles(level)
    power = PowerUp()

    running = True
    while running:

        # =========================
        # DRAW BACKGROUND (IMPORTANT)
        # =========================
        screen.blit(road_img, (0, 0))

        # =========================
        # EVENTS
        # =========================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # =========================
        # PLAYER INPUT
        # =========================
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)

        # =========================
        # VEHICLES
        # =========================
        for vehicle in vehicles:
            vehicle.update()
            vehicle.draw(screen)

            # COLLISION → GAME OVER
            if player.rect.colliderect(vehicle.rect):
                return  # exit game()

        # =========================
        # POWER-UP (COIN)
        # =========================
        power.draw(screen)

        if player.rect.colliderect(power.rect):
            player.stamina = min(player.max_stamina, player.stamina + 30)
            player.score += 10
            power.spawn()

        # =========================
        # NEXT LEVEL
        # =========================
        if player.rect.top <= 0:
            level += 1

            # reset player position
            player.rect.center = (WIDTH // 2, HEIGHT - 60)

            # increase difficulty
            vehicles = create_vehicles(level)

        # =========================
        # DRAW PLAYER + UI
        # =========================
        player.draw(screen)

        font = pygame.font.SysFont("Arial", 28)
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))

        screen.blit(level_text, (650, 20))
        screen.blit(score_text, (650, 50))

        # =========================
        # UPDATE SCREEN
        # =========================
        pygame.display.update()
        clock.tick(60)


# =========================
# MAIN GAME FLOW
# =========================
while True:
    choice = menu.main()

    if choice == "start":
        game()

        result = menu.gameover()

        if result == "restart":
            continue