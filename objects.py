import pygame as pg
from config import *
from resources import Resources
class Block:
    def __init__(self, pos, texture, sc, collider, name):
        self.pos = pos
        self.texture = texture
        self.sc = sc
        self.collider = collider
        self.rect = pg.Rect(0, 0, 0, 0)
        self.name = name
    def draw(self, scroll):
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.pos
        self.sc.blit(self.texture, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        return self
class Removable:
    def __init__(self, pos, texture, sc, collider, name):
        self.pos = pos
        self.texture = texture
        self.sc = sc
        self.collider = True
        self.rect = pg.Rect(0, 0, 0, 0)
        self.removed = False
        self.name = name
    def draw(self, scroll):
        if not self.removed:
            self.rect = self.texture.get_rect()
            self.rect.topleft = self.pos
            self.sc.blit(self.texture, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        return self

    def remove(self):
        self.removed = True

class Door:
    def __init__(self, pos, texture, sc, collider, name):
        self.pos = pos
        self.texture_open = texture[0]
        self.texture_close = texture[1]
        self.sc = sc
        self.collider = True
        self.rect = pg.Rect(0, 0, 0, 0)
        self.opened = False
        self.name = name
        self.timer = 0
    def draw(self, scroll):
        if not self.opened:
            self.rect = self.texture_close.get_rect()
            self.rect.topleft = self.pos
            self.sc.blit(self.texture_close, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        else:
            self.rect = self.texture_open.get_rect()
            self.rect.topleft = self.pos
            self.sc.blit(self.texture_open, (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        return self

    def open(self):
        self.opened = True

