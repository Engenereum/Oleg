import math

import pygame

RES = 1200, 900
CENTER = RES[0] // 2, RES[1] // 2

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

running = True
center = CENTER
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    x, y = 0, 0
    if center[0] < mouse_pos[0]:
        x = 1
    elif center[0] > mouse_pos[0]:
        x = -1
    if center[1] < mouse_pos[1]:
        y = 1
    elif center[1] > mouse_pos[1]:
        y = -1
    center2 = center[0] + 5 * x, center[1] + 5 * y
    a, b = center2
    if math.fabs(center2[0] - mouse_pos[0]) <= 5:
        a = mouse_pos[0]
    if math.fabs(center2[1] - mouse_pos[1]) <= 5:
        b = mouse_pos[1]
    center = a, b

    screen.fill(pygame.color.Color("lightgreen"))

    pygame.draw.circle(screen, pygame.color.Color("red"), center, 50)

    pygame.display.flip()
    clock.tick(60)
