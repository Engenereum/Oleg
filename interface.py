import pygame
from pygame import Surface


class Interface:
    def __init__(self):
        self.surf = Surface((100, 500))
        self.level_font = pygame.font.Font("visitor2.otf", 100)
        self.level_text = self.level_font.render("                 ВОЛНА 1", 1, (255, 255, 255))
        self.hp = pygame.image.load("hp.png")
        self.hp = pygame.transform.scale(self.hp, (500, 400))
        self.clock_delay = 3
        self.border = pygame.image.load("damage_border.png").convert_alpha()
        self.counter = 255

    def draw(self, screen: Surface, count):
        rect = self.level_text.get_rect()
        w = 71
        h = 60
        shift = 93
        for i in range(count):
          pygame.draw.rect(screen, (255,0,0),(shift + i * w, 52, w, h))
        screen.blit(self.hp, (0 * self.hp.get_width(), -100))
        if pygame.time.get_ticks() <= 3 * 1000:
            w, h = screen.get_size()
            screen.blit(self.level_text, (0, 0))
        if pygame.time.get_ticks() > 4 * 1000 and self.counter > 0:
            self.draw_damage(screen)

    def draw_damage(self, screen):
        size = screen.get_size()
        surface = pygame.surface.Surface(size)
        surface.set_alpha(self.counter)
        border = pygame.transform.scale(self.border,size)
        surface.blit(border, (0, 0))
        screen.blit(surface, (0,0))
        self.counter -= 4