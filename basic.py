import pygame
import os

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MotionSensor')
running = True

player = pygame.image.load(os.path.join('assets', 'ME.jpg')).convert()
lit_room = pygame.image.load(os.path.join('assets', 'Background1.png'))
non_lit_room = pygame.image.load(os.path.join('assets', 'Background2.png'))
player_pos = pygame.Vector2(0, 0)
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (player_pos[0] > 411 and player_pos[0] < 900) and (player_pos[1] > 417 and player_pos[1] < 523):
        screen.blit(non_lit_room, (0, 0))
    else:
        screen.blit(lit_room, (0, 0))
    screen.blit(player, (player_pos))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()