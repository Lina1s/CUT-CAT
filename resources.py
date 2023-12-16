import pygame as pg
from config import *


class Resources:
    """
       Класс Resources предназначен для загрузки и хранения ресурсов игры, таких как изображения персонажей, фона, текстур.
       Этот класс централизует ресурсы, чтобы они были легко доступны из других частей игры.

       Атрибуты:
           player_image_r (list): Список изображений игрока, движущегося вправо.
           player_image_l (list): Список изображений игрока, движущегося влево, полученных
                                  путем горизонтального отражения изображений из player_image_r.
           player_img_dead (list): Список изображений игрока в состоянии "мертв", с двумя вариантами
                                   направления (направо и налево).
           background (list): Список изображений фонов для уровней игры.
           textures (dict): Словарь, содержащий текстуры для различных игровых элементов,
                            таких как земля, препятствия и собираемые предметы.
                            Ключи словаря указывают на тип элемента (например, 'ground_bottom' или 'fish'),
                            а значения — это загруженные и масштабированные изображения.
           texture_symbols (dict): Словарь, сопоставляющий символы с соответствующими текстурами для
                                   отображения уровней. Используется для быстрой конвертации символов уровня
                                   в графические элементы на экране.
       """

    def __init__(self):
        self.player_image_r = [pg.image.load("cat3.PNG").convert_alpha(),
                               pg.image.load("cat4.PNG").convert_alpha(),
                               pg.image.load("cat6.PNG").convert_alpha(),
                               pg.image.load("cat7.PNG").convert_alpha()]

        self.player_image_l = [pg.transform.flip(self.player_image_r[0], True, False),
                               pg.transform.flip(self.player_image_r[1], True, False),
                               pg.transform.flip(self.player_image_r[2], True, False),
                               pg.transform.flip(self.player_image_r[3], True, False)]

        self.player_img_dead = [pg.image.load("cat_d.png").convert_alpha()]
        self.player_img_dead.append(pg.transform.flip(self.player_img_dead[0], True, False))

        self.background = [pg.transform.scale(pg.image.load("aaa.png"), (WIDTH, HEIGHT)).convert_alpha(),
                           pg.transform.scale(pg.image.load("fon.png"), (WIDTH, HEIGHT)).convert_alpha(),
                           pg.transform.scale(pg.image.load("mounth.png"), (WIDTH, HEIGHT)).convert_alpha()]

        self.textures = {"ground_bottom": pg.transform.scale(pg.image.load("ground_bottom.png"),
                                                             (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "ground_top": pg.transform.scale(pg.image.load("ground_top.png"),
                                                          (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "y": pg.transform.scale(pg.image.load("y.png"), (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "box": pg.transform.scale(pg.image.load("box.png"), (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "heart": pg.transform.scale(pg.image.load("heart.png"),
                                                     (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "fish": pg.transform.scale(pg.image.load("fish.png"), (BLOK_SIZE, BLOK_SIZE)).convert_alpha(),
                         "door": [pg.transform.scale(pg.image.load("open_door.png"),
                                                     (BLOK_SIZE * 3, BLOK_SIZE * 4)).convert_alpha(),
                                  pg.transform.scale(pg.image.load("close_door.png"),
                                                     (BLOK_SIZE * 3, BLOK_SIZE * 4)).convert_alpha()],
                         "present": pg.transform.scale(pg.image.load("milk.png"),
                                                       (BLOK_SIZE, BLOK_SIZE)).convert_alpha()}
        self.texture_symbols = {"+": self.textures["box"],
                                ".": self.textures["y"],
                                "#": self.textures["ground_bottom"],
                                "=": self.textures["ground_top"],
                                "h": self.textures["heart"],
                                "f": self.textures["fish"],
                                "|": self.textures["door"],
                                "*": self.textures["present"]}
