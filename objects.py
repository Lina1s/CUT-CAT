import pygame as pg
from config import *
from resources import Resources
class Block:
    def __init__(self, pos, texture_name, sc, collider):
        self.pos = pos
        self.texture_name = texture_name
        self.sc = sc
        self.colider = collider
    def draw(self, scroll):
        rect: pg.Rect = Resources.texture_symbols[self.texture_name].get_rect()
        rect.topleft = self.pos
        self.sc.blit(Resources.texture_symbols[self.texture_name], (self.pos[0] - scroll[0], self.pos[1] - scroll[1]))
        if self.colider:
            return rect
        return