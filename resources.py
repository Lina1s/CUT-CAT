from  config import *
import pygame as pg

class Resources:

        player_image_r = [pg.image.load("cat3.PNG"),
                          pg.image.load("cat4.PNG"),
                          pg.image.load("cat6.PNG"),
                          pg.image.load("cat7.PNG")]


        player_image_l = [pg.transform.flip(player_image_r[0], True, False),
                          pg.transform.flip(player_image_r[1], True, False),
                          pg.transform.flip(player_image_r[2], True, False),
                          pg.transform.flip(player_image_r[3], True, False)]



        background = [pg.transform.scale(pg.image.load("aa.png"), (WIDTH, HEIGHT)),
                      pg.transform.scale(pg.image.load("fon.png"), (WIDTH, HEIGHT)),
                      pg.transform.scale(pg.image.load("kr.png"), (WIDTH, HEIGHT))]

        textures = {"ground_bottom": pg.transform.scale(pg.image.load("ground_bottom.png"), (BLOK_SIZE, BLOK_SIZE)),
                    "ground_top": pg.transform.scale(pg.image.load("ground_top.png"), (BLOK_SIZE, BLOK_SIZE)),
                    "y": pg.transform.scale(pg.image.load("y.png"), (BLOK_SIZE, BLOK_SIZE)),
                    "zabor": pg.transform.scale(pg.image.load("zabor.png"), (BLOK_SIZE, BLOK_SIZE)),
                    "box": pg.transform.scale(pg.image.load("box.png"), (BLOK_SIZE, BLOK_SIZE))}

        texture_symbols = {"+": textures["box"],
                           ".": textures["y"],
                           "#": textures["ground_bottom"],
                           "=": textures["ground_top"],
                           "%": textures["zabor"]}