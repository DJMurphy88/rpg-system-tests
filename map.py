import pygame
from pygame.locals import *
import pytmx

FILE = "Data/Grass_v1.png"

class Level:
    def __init__(self, map_file):
        self.map_object = pytmx.load_pygame(map_file)
        self.layers = []
        self.level_shift = [0, 0]

        for layer in range(len(self.map_object.layers)):
            self.layers.append(Layer(index=layer, map_object=self.map_object))

    def shift_map(self, x, y):
        self.level_shift[0] += x
        self.level_shift[1] += y

        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += x
                tile.rect.y += y

    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)

class Layer:
    def __init__(self, index, map_object):
        self.index = index
        self.tiles = pygame.sprite.Group()
        self.map_object = map_object

        for x in range(self.map_object.width):
            for y in range(self.map_object.height):
                img = self.map_object.get_tile_image(x, y, self.index)
                if img:
                    self.tiles.add(Tile(img, (x * self.map_object.tilewidth), (y * self.map_object.tileheight)))

    def draw(self, screen):
        self.tiles.draw(screen)

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
