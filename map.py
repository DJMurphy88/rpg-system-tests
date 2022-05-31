import pygame.image
import numpy as np

# Tileset class, loads tileset from file, divides it into tiles,
# and populates a list with the tiles
class Tileset:
    def __init__(self, file, size=(32, 32), margin=1, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing

        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))

    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'

class Tilemap:
    def __init__(self, tileset, size=(10, 20), rect=None):
        self.tileset = tileset
        self.size = size
        self.map = np.zeros(size, dtype=int)

        h, w = self.size
        self.image = pygame.Surface((32*w, 32*h))
        if rect:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = self.image.get_rect()

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*32, i*32))

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
