import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Лох")

x = 0
y = 2
w = 10
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += 0.1
    if x > 600:
        x = -50
    y += 0.1
    if y > 600:
        y = -50

    screen.fill((255, 225, 225))

    # Чёрный
    pygame.draw.circle(screen, (0, 0, 0), (x, 250), 20)
    # Синий
    pygame.draw.circle(screen, (0, 0, 225), (250, y), 20)
    # Зелёный
    pygame.draw.circle(screen, (0, 225, 0), (x, x), 20)
    # Красный
    pygame.draw.circle(screen, (225, 0, 0), (500 - x, x), 20)
    # Голубой
    pygame.draw.circle(screen, (0, 225, 225), (500 - x, 250), 20)
    # Розовый
    pygame.draw.circle(screen, (225, 0, 225), (250, 500 - y), 20)
    # Жёлтый
    pygame.draw.circle(screen, (225, 225, 0), (500 - x, 500 - x), 20)
    # Оранжевый
    pygame.draw.circle(screen, (255, 69, 0), (x, 500 - x), 20)

    pygame.display.update()
