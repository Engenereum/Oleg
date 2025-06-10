import pygame



pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Лох")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((225,225,0))

    pygame.draw.rect(screen, (0,225,0),(100,100,100,100))
    pygame.draw.circle(screen, (50,50,50),(350,150), 50)
    pygame.draw.line(screen, (0, 225, 225), (0,0), (500,300), 50)
    pygame.draw.polygon(screen, (50, 225, 50), [(50,50),(100,100),(70,70)], 2)


    pygame.display.update()