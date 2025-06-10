import pygame
from pygame import Rect

pygame.init()

screen = pygame.display.set_mode((300, 300))

num = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    step = 300 // num
    screen.fill((0, 0, 0))

    for i in range(num):
        rect = Rect(i * step // 2, 0, 300 - i * step, 300)
        pygame.draw.ellipse(screen, color=pygame.color.Color('White'), rect=rect, width=1)
    for i in range(num):
        rect = Rect(0, i * step // 2, 300, 300 - i * step)
        pygame.draw.ellipse(screen, color=pygame.color.Color('White'), rect=rect, width=1)
    pygame.display.flip()
