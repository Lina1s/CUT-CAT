import pygame as pg
from other import *
from config import *
from objects import *


class Player:
    """"
     Класс для управления игроком в игре, использующий библиотеку Pygame.

    :param sc: Экран, на котором будут отображаться изображения игрока.
    :param player_images_r: Список изображений игрока, идущего вправо.
    :param player_images_l: Список изображений игрока, идущего влево.
    :param player_img_dead: Два состояния игрока после проигрыша.
    :param font: Шрифт для отображения текста в игре.

    Игрок обладает следующими характеристиками::

        self.movement - вектор (x, y) движения игрока на экране.
        self.old_dir - вектор (x, y) предыдущего движения игрока, используется для определения направления статического изображения.
        self.rect - Pygame прямоугольник, задающий позиционирование в мире игры.
        self.anim_count - счетчик для анимации движения игрока.
        self.is_run - булево значение, истина если игрок в движении.
        self.delta_time - время, прошедшее с последнего обновления.
        self.scroll_x, self.scroll_y - значения прокрутки экрана игры для корректировки отображения.

    Физические свойства игрока::

        self.air_time - время, прошедшее с последнего контакта с землей, используется для расчетов прыжка и падения.
        self.is_ground - булево значение, истина если игрок стоит на земле.

    Другие свойства::

        self.hp - уровень здоровья игрока.
        self.collected_fish - количество собранных игроком рыб.
        self.font - шрифт, используемый для отображения текста.
        self.return_to_main_data - данные, возвращаемые в главный цикл игры.

    .. method:: __init__(sc, player_images_r, player_images_l, player_img_dead, font)

        Инициализация нового объекта класса `Player`.

    .. method:: draw()

        Отображает текущее изображение игрока на экране в зависимости от его состояния и направления движения.

    .. method:: update(delta_time, blocks, scroll)

        Обновляет состояние игрока, включая его физическое положение и сбор предметов. Возвращает данные обратно в главный цикл игры.

        :param delta_time: Время прошедшее с последнего вызова обновления.
        :param blocks: Спрайты блоков, используемые для определения столкновений.
        :param scroll: Координаты прокрутки экрана.

    .. method:: change_dir()

        Определяет изменение направления движения игрока на основе нажатых клавиш.

    .. method:: get_jump()

        Проверяет условие для выполнения прыжка и возвращает булево значение.

    .. method:: physics(blocks)

        Обрабатывает физику движения игрока, включая прыжки, падения и столкновения с блоками.

        :param blocks: Спрайты блоков, используемые для определения столкновений.

    .. method:: get_collision(blocks)

        Проверяет столкновения игрока с блоками и обрабатывает полученные результаты.

        :param blocks: Спрайты блоков, используемые для определения столкновений.
"""

    def __init__(self, sc, player_images_r, player_images_l, player_img_dead, font):
        self.sc = sc
        self.imgs_r = player_images_r
        self.imgs_l = player_images_l
        self.imgs_dead = player_img_dead

        self.movement = [0, 0]
        self.old_dir = [0, 0]
        self.rect = self.imgs_l[0].get_rect()
        self.rect.topleft = [200, 300]
        self.anim_count = 0
        self.is_run = False
        self.delta_time = 0
        self.scroll_x = 0
        self.scroll_y = 0

        # Физика
        self.air_time = 0
        self.is_ground = False

        # Другое
        self.hp = 9
        self.collected_fish = 0
        self.font = font
        self.return_to_main_data = {}

    def draw(self):
        self.anim_count %= 400
        if self.hp > 0:
            if self.is_run:
                if self.movement[0] > 0:
                    self.sc.blit(self.imgs_r[int(self.anim_count * 0.001 * 6)],
                                 (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
                if self.movement[0] < 0:
                    self.sc.blit(self.imgs_l[int(self.anim_count * 0.001 * 6)],
                                 (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            else:
                if self.old_dir[0] > 0:
                    self.sc.blit(self.imgs_r[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
                elif self.old_dir[0] < 0:
                    self.sc.blit(self.imgs_l[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
        else:
            if self.old_dir[0] > 0:
                self.sc.blit(self.imgs_dead[1], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))
            else:
                self.sc.blit(self.imgs_dead[0], (self.rect.x - self.scroll_x, self.rect.y - self.scroll_y))

    def update(self, delta_time, blocks, scroll):
        self.return_to_main_data = {}
        self.scroll_x = scroll[0]
        self.scroll_y = scroll[1]
        self.delta_time = delta_time
        if self.hp > 0:
            self.change_dir()
        self.anim_count += delta_time
        self.physics(blocks)
        return self.return_to_main_data

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
        if keys[pg.K_SPACE] and self.hp > 0:
            return True
        return False

    def physics(self, blocks):
        self.air_time += -self.delta_time * 0.001
        self.movement[1] = GRAVITY * self.air_time / 3
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
                self.air_time = 0.3  # скорость прыжка
        self.is_ground = False

    def get_collision(self, blocks):
        collide = []
        for col in blocks:
            if col.collider:
                if self.rect.colliderect(col.rect):
                    if isinstance(col, Removable):
                        if not col.removed:
                            if col.name == "h":
                                self.hp += 9
                            elif col.name == "f":
                                self.collected_fish += 1
                            col.remove()
                    elif isinstance(col, Door):
                        if not col.opened:
                            if self.collected_fish >= 5:
                                self.collected_fish -= 5
                                col.open()
                            else:
                                self.return_to_main_data = {
                                    "message": [2, "Collect all the fish to open the door"]}
                                collide.append(col.rect)
                    elif col.name == "*":
                        self.return_to_main_data = {
                            "message_1": [2, "WIN"]}
                    else:
                        collide.append(col.rect)

        return collide
