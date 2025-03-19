import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тир Game")
icon = pygame.image.load("image/img_1.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("image/img.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(99, 255), random.randint(99, 255), random.randint(9, 255))



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





pygame.quit()