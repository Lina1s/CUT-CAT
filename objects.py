import pygame as pg
from config import *
from resources import Resources


class Block:
    """
       Класс Block предназначен для представления отдельного блока в игре - базовых компонентов уровня,
       из которых строится игровая среда. Блок может представлять собой элемент ландшафта, препятствие,
       платформу или любой другой статический объект в игровом мире.

       Атрибуты:
           pos (tuple): Кортеж, содержащий координаты блока (x, y) на игровом экране.
           texture (pygame.Surface): Поверхность Pygame, которая является изображением (текстурой) блока.
           sc (pygame.Surface): Поверхность Pygame, на которую должен быть нарисован блок.
           collider (bool): Флаг, указывающий, должна ли учитываться столкновения для этого блока.
           rect (pygame.Rect): Объект Rect, представляющий прямоугольную область блока. Используется для определения столкновений.
           name (str): Имя или идентификатор блока, который может быть использован для выполнения специфических действий или логики.

       Методы:
           __init__(self, pos, texture, sc, collider, name): Этот конструктор принимает начальные параметры и настраивает блок.
           draw(self, scroll): Отрисовывает блок с учетом переданного смещения прокрутки (движение камеры или персонажа).
       """

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
    """
        Класс Removable расширяет функционал базового класса Block, добавляя возможность удаления блока из игрового пространства.
        Он предназначен для представления объектов, которые могут быть удалены во время выполнения игры, например, блоки, разрушаемые
        игроком или исчезающие после определенного события.

        Атрибуты:
            pos (tuple): Кортеж, содержащий начальные координаты объекта (x, y) на игровом экране.
            texture (pygame.Surface): Изображение объекта, представленное в виде поверхности Pygame.
            sc (pygame.Surface): Поверхность Pygame, на которую объект должен быть нарисован.
            collider (bool): Атрибут всегда установлен в True и указывает, что объект учитывается в системе столкновений.
            rect (pygame.Rect): Прямоугольник Pygame, представляющий объект и используемый для обнаружения столкновений.
            removed (bool): Состояние объекта, которое определяет, был ли он удален (True) или нет (False).
            name (str): Название или идентификатор объекта, который может использоваться для особых действий или логики игры.

        Методы:
            __init__(self, pos, texture, sc, collider, name): Конструктор инициализирует объект с начальными параметрами.
            draw(self, scroll): Отрисовывает объект с учетом смещения прокрутки, если объект не был удален.
            remove(self): Устанавливает состояние 'removed' объекта в True, что делает его невидимым и неактивным в игре.
        """

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
    """
        Класс Door используется для создания и управления дверью в игре, которая может быть открыта или закрыта.

        Атрибуты:
            pos (tuple): Кортеж, содержащий координаты (x, y), где дверь отрисовывается на игровом экране.
            texture_open (pygame.Surface): Изображение открытой двери, представленное в виде поверхности Pygame.
            texture_close (pygame.Surface): Изображение закрытой двери, представленное в виде поверхности Pygame.
            sc (pygame.Surface): Поверхность Pygame, на которую дверь будет нарисована.
            collider (bool): Значение, указывающее, следует ли учитывать дверь в системе столкновений (всегда True).
            rect (pygame.Rect): Прямоугольник Pygame, представляющий дверь и используемый для обнаружения столкновений.
            opened (bool): Состояние двери, которое определяет, открыта она (True) или закрыта (False).
            name (str): Название или идентификатор двери, который может использоваться в логике игры.
            timer (int): Таймер для управления временем или задержками в действиях с дверью (не используется в предоставленном коде).

        Методы:
            __init__(self, pos, texture, sc, collider, name): Конструктор инициализирует дверь с начальными параметрами.
            draw(self, scroll): Отрисовывает дверь в зависимости от её состояния (открыта/закрыта), учитывая смещение прокрутки.
            open(self): Изменяет состояние двери на открытое.

        """

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
