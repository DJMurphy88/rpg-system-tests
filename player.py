import pygame
from settings import *
from pygame.locals import *

from settings import *

SPEED = 8

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = SpriteSheet('Data/player_test.png')

        self.forward = self.sprites.image_at((0, 0, 32, 32))

        self.image = self.forward
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0
        self.direction = pygame.math.Vector2()

        self.current_map = None

    def x_axis(self, direction):
        if direction == 1:
            self.change_x = 1
        elif direction == -1:
            self.change_x = -1
        elif direction == 0:
            self.change_x = 0

    def y_axis(self, direction):
        if direction == 1:
            self.change_y = 1
        elif direction == -1:
            self.change_y = -1
        elif direction == 0:
            self.change_y = 0

    def collision(self):
        return pygame.sprite.spritecollide(self, self.current_map.layers[MAP_COLLISION_LAYER].tiles, False)

    def update(self):

        self.rect.x += self.change_x * SPEED

        collision_tiles = self.collision()

        for tile in collision_tiles:
            if self.change_x > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right

        if self.rect.right >= SIZE[0] - 200:
            difference = self.rect.right - (SIZE[0] - 200)
            self.rect.right = SIZE[0] - 200
            self.current_map.shift_map(-difference, 0)

        if self.rect.left <= 200:
            difference = 200 - self.rect.left
            self.rect.left = 200
            self.current_map.shift_map(difference, 0)

        self.rect.y += self.change_y * SPEED

        collision_tiles = self.collision()

        for tile in collision_tiles:
            if self.change_y > 0:
                self.rect.bottom = tile.rect.top
            else:
                self.rect.top = tile.rect.bottom

        if self.rect.bottom >= SIZE[1] - 200:
            difference = self.rect.bottom - (SIZE[1] - 200)
            self.rect.bottom = SIZE[1] - 200
            self.current_map.shift_map(0, -difference)

        if self.rect.top <= 200:
            difference = 200 - self.rect.top
            self.rect.top = 200
            self.current_map.shift_map(0, difference)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class SpriteSheet:
    def __init__(self, sprite_file):
        self.sheet = pygame.image.load(sprite_file)

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        return image
