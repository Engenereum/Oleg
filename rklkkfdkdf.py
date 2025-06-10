import pygame
from pygame import Rect


class Triangle:
    def __init__(self, point1: tuple, point2: tuple, point3: tuple):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.b = max(self.p1[1], self.p2[1], self.p3[1])

    def draw(self, screen, color, width=1):
        pygame.draw.line(screen, color, self.p1, self.p2, width)
        pygame.draw.line(screen, color, self.p2, self.p3, width)
        pygame.draw.line(screen, color, self.p3, self.p1, width)

    def move(self, x, y):
        self.p1 = self.p1[0] + x, self.p1[1] + y
        self.p2 = self.p2[0] + x, self.p2[1] + y
        self.p3 = self.p3[0] + x, self.p3[1] + y
        self.b = max(self.p1[1], self.p2[1], self.p3[1])

    def draw_filled(self, screen, color):
        pygame.draw.polygon(screen, color, [self.p1, self.p2, self.p3])

    def set_botton(self, y):
        delta_y = self.b - y
        self.move(0, delta_y)


if __name__ == "__main__":
    pygame.init()
    SIZE = 900, 600
    screen = pygame.display.set_mode(SIZE)
    running = True
    is_jump = False
    jump_force = 0
    gravity_force = 3
    trg = Triangle((50, 50), (0, 150), (100, 150))
    clock = pygame.time.Clock()
    drawing = False
    last_pos = None
    points = []
    while running:

        #buttons = pygame.mouse.get_pressed()
        #if buttons[0]:
        #    print("1")
        #if buttons[2]:
        #    print("2")


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            trg.move(0, -10)
        if keys[pygame.K_d]:
            trg.move(10, 0)
        if keys[pygame.K_a]:
            trg.move(-10, 0)
        # if keys[pygame.K_s]:
        #    trg.move(0, 10)
        if keys[pygame.K_SPACE]:
            if is_jump:
                jump_force = -50
        if trg.b + jump_force <= 550:
            trg.move(0, jump_force)
            jump_force = jump_force + gravity_force
            is_jump = False
        else:
            trg.set_botton(550)
            jump_force = 0
            is_jump = True

        screen.fill(pygame.color.Color("lightskyblue"))
        rect = Rect(0, 550, 900, 50)
        pygame.draw.rect(screen, pygame.color.Color("green"), rect)
        trg.draw(screen, pygame.color.Color("black"), width=1)
        trg.draw_filled(screen, pygame.color.Color("red"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    print("Бееее")
                    last_pos = event.pos
                    drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    print("оаовыа")
                    drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if last_pos:
                        #pygame.draw.line(screen, pygame.color.Color("red"), last_pos, event.pos, 5)
                        points.append(last_pos)
                        last_pos = event.pos
                    else:
                        last_pos = event.pos
        if len(points) > 1:
            pygame.draw.lines(screen, pygame.color.Color("red"), False, points, 100)
        pygame.display.flip()
        clock.tick(60)
