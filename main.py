import pygame, sys, random
from pygame.math import Vector2

class Game(object):
    def __init__(self):
        #konfiguracja zegara - maksymalna ilosc tykniec na sekunde
        self.tps_max = 100.0

        #inicjalizacja pygame
        pygame.init()
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        #konfiguracja okna
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Giera na kole')

        self.player = Player(self)

        #glowna petla gry
        while True:
            #sprawdzamy eventy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            self.tps_delta += self.tps_clock.tick() / 1000.0

            #tykanie zegara
            while self.tps_delta > 1 /self.tps_max:
                self.tick()
                self.tps_delta -= 1/ self.tps_max

            #rysowanie
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()

class Player(object):
    def __init__(self, game):
        self.game = game
        self.speed = 1.3

        size = self.game.screen.get_size()

        self.pozycja = Vector2(size[0]/2, size[1]/2)
        self.predkosc = Vector2(0, 0)
        self.przyspieszenie = Vector2(0, 0)


    def tick(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.pozycja.y -= self.speed
        if pressed[pygame.K_s]:
            self.pozycja.y += self.speed
        if pressed[pygame.K_a]:
            self.pozycja.x -= self.speed
        if pressed[pygame.K_d]:
            self.pozycja.x += self.speed

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 150, 255), pygame.Rect(self.pozycja.x, self.pozycja.y, 50, 50))

if __name__ == "__main__":
    Game()