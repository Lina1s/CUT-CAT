from config import *
import pygame as pg
from objects import Block
class Level:
    def __init__(self, sc, textures, level_offset):
        self.level = []
        with open("level", "r") as file:
            for line in file.readlines():
                line = line.replace("\n", "")
                self.level.append(line)
        self.ignored_collision = ["%", "."]
        self.sc = sc
        self.types = {"#": Block,
                      ".": Block,
                      "+": Block,
                      "=": Block,
                      "%": Block,}
        self.level_offset = level_offset
        self.level_blocks = []
        self.start()
    def start(self):
        colliders = []
        for i, y in enumerate(self.level):
            for j, x in enumerate(y):
                if x not in self.ignored_collision:
                    pos = [j*BLOK_SIZE - self.level_offset[0], i*BLOK_SIZE - self.level_offset[1]]
                    self.level_blocks.append(self.types[x](pos, x, self.sc, True))

    def update(self, scroll):
        colliders = []
        for i, y in enumerate(self.level_blocks):
            res = y.draw(scroll)
            if res is not None:
                colliders.append(res)
        return colliders
