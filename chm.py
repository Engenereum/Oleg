import pygame

pygame.init()

size, num = int(input()), int(input())
square = size / num
is_black = True
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Лох")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(num):
        for j in range(num):
            if is_black:
                color = (0,0,0)
            else:
                color = (225,225,225)
            is_black = not is_black
            pygame.draw.rect(screen, color, (i * square, j * square, square, square))


    pygame.display.update()
