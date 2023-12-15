import pygame
import pygame as pg
from config import *


class Player:
    def __init__(self, sc, player_images_r, player_images_l):
        self.sc = sc
        self.imgs_r = player_images_r
        self.imgs_l = player_images_l

        self.movement = [0, 0]
        self.old_dir = [0, 0]
        self.rect = self.imgs_l[0].get_rect()
        self.rect.topleft = [200, -100]
        self.anim_count = 0
        self.is_run = False
        self.delta_time = 0
        self.scroll_x = 0
        self.scroll_y = 0

        # Физика
        self.air_time = 0
        self.is_ground = False

    def draw(self):
        self.anim_count %= 400
        if self.is_run:
            if self.movement[0] > 0:
                self.sc.blit(self.imgs_r[int(self.anim_count*0.001*6)], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            if self.movement[0] < 0:
                self.sc.blit(self.imgs_l[int(self.anim_count*0.001*6)], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
        else:
            if self.old_dir[0] > 0:
                self.sc.blit(self.imgs_r[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            elif self.old_dir[0] < 0:
                self.sc.blit(self.imgs_l[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))

    def update(self, delta_time, blocks, scroll):
        self.scroll_x = scroll[0]
        self.scroll_y = scroll[1]
        self.delta_time = delta_time
        self.change_dir()
        self.anim_count += delta_time
        self.physics(blocks)

    def change_dir(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.movement[0] = -1
        elif keys[pg.K_RIGHT]:
            self.movement[0] = 1
        else:
            if self.movement[0] != 0:
                self.old_dir[0] = self.movement[0]
            self.is_run = False
            self.movement[0] = 0
        if self.movement[0] != 0:
            self.is_run = True

    def get_jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            return True
        return False
    def physics(self, blocks):
        self.air_time += -self.delta_time * 0.001
        self.movement[1] = GRAVITY * self.air_time/3
        self.rect.x += self.movement[0] * self.delta_time
        collide = self.get_collision(blocks)
        for col in collide:
            if self.movement[0] > 0:
                self.rect.right = col.left
            elif self.movement[0] < 0:
                self.rect.left = col.right

        self.rect.y += self.movement[1] * self.delta_time
        collide = self.get_collision(blocks)
        for col in collide:
            if self.movement[1] > 0:
                self.rect.bottom = col.top
                self.is_ground = True
            elif self.movement[1] < 0:
                self.rect.top = col.bottom
        if self.is_ground:
            self.air_time = 0
            if self.get_jump():
                self.air_time = 0.3 #скорость прыжка
        self.is_ground = False
    def get_collision(self, blocks):
        collide = []
        for col in blocks:
            if col:
                if self.rect.colliderect(col):
                    collide.append(col)
        return collide
