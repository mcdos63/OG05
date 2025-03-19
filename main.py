import pygame
import random

# Класс для создания частиц
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(6, 10)  # Увеличен начальный размер частиц
        self.speed_x = random.uniform(-0.5, 0.5)  # Уменьшена скорость по X
        self.speed_y = random.uniform(-1, 0.25)  # Уменьшена скорость по Y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size -= 0.03  # Уменьшена скорость уменьшения размера

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Список для хранения частиц
particles = []

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тир Game")
icon = pygame.image.load("image/img_2.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("image/img.png")
target_width = 70
target_height = 80
target_image = pygame.transform.scale(target_image, (target_width, target_height))
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(99, 255), random.randint(99, 255), random.randint(9, 255))

running = True

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                for _ in range(12):
                    particles.append(Particle(target_x + target_width//2, target_y + target_height//2, (255, 0, 0)))


    # Обновление и отрисовка частиц
    for particle in particles[:]:
        particle.update()
        particle.draw(screen)

    # Удаление частиц, размер которых стал меньше или равен 0
    particles = [particle for particle in particles if particle.size > 0]

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()
