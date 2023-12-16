from config import *
import pygame as pg
from objects import *


class Level:
    """
       Класс Level представляет игровой уровень в игре. Он отвечает за загрузку структуры уровня из файла,
       инициализацию блоков уровня, а также их обновление и отрисовку на экране.

       Атрибуты:
           sc (pygame.Surface): Поверхность Pygame, на которой будет отображаться уровень.
           level (list): Список, содержащий структуру уровня, загруженный из файла. Каждый элемент списка является строкой из символов, представляющих различные типы блоков.
           ignored_collision (list): Список символов, блоки с которыми следует игнорировать при обработке столкновений.
           types (dict): Словарь, сопоставляющий символы с классами блоков, которые нужно инициализировать на их месте. Включает различные типы блоков, такие как стандартные, удаляемые, двери и т.д.
           textures (dict): Словарь текстур, сопоставляющий символы с их соответствующими изображениями. Используется при инициализации блоков.
           level_offset (tuple): Смещение начальной позиции уровня относительно верхнего левого угла экрана. Используется для создания параллакса или центровки уровня.
           level_blocks (list): Список экземпляров блоков уровня, инициализированных и готовых к отображению.

       Методы:
           __init__(self, sc, textures, level_offset): Инициализирует экземпляр Level, загружая структуру из файла и подготавливая блоки соответственно.
           start(self): Инициализирует блоки уровня на основе структуры, загруженной из файла. Игнорирует блоки, обозначенные для игнорирования при обработке столкновений.
           update(self, scroll): Обновляет позиции всех блоков уровня в соответствии со смещением прокрутки и отрисовывает их на экране.
       """

    def __init__(self, sc, textures, level_offset):
        # Loading Level  layout
        self.sc = sc

        self.level = []
        with open("level", "r") as file:
            for line in file.readlines():
                line = line.replace("\n", "")
                self.level.append(line)

        self.ignored_collision = ["."]
        self.types = {"#": Block,
                      ".": Block,
                      "=": Block,
                      "+": Block,
                      "%": Block,
                      "h": Removable,
                      "f": Removable,
                      "|": Door,
                      "*": Block}
        self.textures = textures

        self.level_offset = level_offset
        self.level_blocks = []

        self.start()

    def start(self):
        for i, y in enumerate(self.level):
            for j, x in enumerate(y):
                if x not in self.ignored_collision:
                    pos = [j * BLOK_SIZE - self.level_offset[0], i * BLOK_SIZE - self.level_offset[1]]
                    self.level_blocks.append(self.types[x](pos, self.textures[x], self.sc, True, x))

    def update(self, scroll):
        objects = []
        for i, y in enumerate(self.level_blocks):
            res = y.draw(scroll)
            objects.append(res)
        return objects
