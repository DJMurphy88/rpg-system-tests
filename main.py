# Main program for testing systems
from objects import *
import pygame
import sys

import player
from map import *
from settings import *

MAP = "Data/Test.tmx"

class Game:
    def __init__(self):
        self.current_map_number = 0
        self.maps = []
        self.maps.append(Level(MAP))
        self.current_map = self.maps[self.current_map_number]

        self.player = player.Player(608, 448)
        self.player.current_map = self.current_map

    def process_event(self):
        keys = pygame.key.get_pressed()

        # Processing of y-axis input
        if keys[DOWN]:
            self.player.y_axis(1)
        elif keys[UP]:
            self.player.y_axis(-1)
        else:
            self.player.y_axis(0)

        # Processing of x-axis input
        if keys[RIGHT]:
            self.player.x_axis(1)
        elif keys[LEFT]:
            self.player.x_axis(-1)
        else:
            self.player.x_axis(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == EXIT:
                    return False

        return True

    def movement(self):
        self.player.update()

    def draw(self, screen):
        screen.fill(BG)
        self.current_map.draw(screen)
        self.player.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("RPG Testing")
    clock = pygame.time.Clock()
    running = True
    game = Game()

    while running:
        running = game.process_event()
        game.movement()
        game.draw(screen)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
