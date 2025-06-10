import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Лох")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 0, 0))
    pygame.draw.line(screen, (255, 225, 225), (0, 0), (500, 500), 50)
    pygame.draw.line(screen, (255, 225, 225), (500, 0), (0, 500), 50)
    pygame.draw.line(screen, (255, 225, 225), (250, 0), (250, 500), 40)
    pygame.draw.line(screen, (255, 225, 225), (0, 250), (500, 250), 40)
    pygame.display.update()
