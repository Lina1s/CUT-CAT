import pygame as pg
import sys
from knopka import ImageKnopka
from player import Player
from config import *
from level import Level
from other import *
from resources import Resources

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
main_background = pg.image.load("back1.jpg")
pg.display.set_caption("Cut cat")
clock = pg.time.Clock()
FPS = 60

pg.mixer.music.load("meoww.mp3")

rsc = Resources()
main_font = pg.font.SysFont("Bauhaus 93", 30)

player = Player(sc, rsc.player_image_r, rsc.player_image_l, rsc.player_img_dead, main_font)


def main_menu():
    """
       Функция `main_menu` запускает главное меню игры, предлагая опции для запуска новой игры
       или выхода из игры.

       В этой функции создаются две кнопки (`lapa` и `door`), которые реагируют на события пользователя,
       такие как наведение мыши и клики. При активации определенных событий, функция `new_game` может
       быть вызвана или приложение может быть закрыто.

       При каждой итерации основного цикла функции, экран `sc` очищается и затем перерисовывается с учетом
       изменений состояния кнопок и других элементов интерфейса.

       Основные шаги функции:
       - Инициализация кнопок с помощью класса `ImageKnopka`.
       - Очистка экрана и отображение фона меню.
       - Вывод на экран заголовка игры.
       - Обработка системных событий Pygame (например, закрытие окна).
       - Обработка событий, связанных с бизнес-логикой игры (например, начало новой игры).
       - Обновление визуального состояния кнопок.
       - Отображение изменений на экране.

       Кнопки:
       - `lapa`: При клике на эту кнопку происходит вызов функции `new_game`, которая должна начать новую игру.
       - `door`: При активации этой кнопки игра закрывается.

       """
    lapa = ImageKnopka(WIDTH / 2 - (190 / 2), 200, 200, 150, "", "lapa.png", "lapa1.png", "meow.mp3")
    door = ImageKnopka(WIDTH / 2 - (125 / 2), 350, 100, 100, "", "door.png", "door1.png", "meow.mp3")
    running = True
    while running:
        sc.fill((0, 0, 0))
        sc.blit(main_background, (0, 0))
        font = pg.font.SysFont('Bauhaus 93', 70)
        text_surface = font.render("CUT CAT", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(570, 80))
        sc.blit(text_surface, text_rect)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if ev.type == pg.USEREVENT and ev.button == lapa:
                new_game()
            if ev.type == pg.USEREVENT and ev.button == door:
                running = False
                pg.quit()
                sys.exit()
            for ld in [lapa, door]:
                ld.handle_event(ev)
        for ld in [lapa, door]:
            ld.check_hover((pg.mouse.get_pos()))
            ld.draw(sc)
        pg.display.flip()


def new_game():
    """
        Функция: new_game
        Модуль: Игровой модуль для Pygame

        Описание:
        Запускает главный игровойцикл.Эта функция управляет логикойи гры, рендерингом, отслеживанием ввода пользователя и музыкальным сопровождением.

        Процесс работы
        Запускается фоновая музыка, которая проигрываетсяна повторении.
        Цикл продолжается бесконечно, пока не будет выполнено действие выхода.
        Отслеживаются системные события для проверки запроса на pакрытие.
        В каждом кадре обновляется состояние игрока, включая убыль егоздоровья.
        Позиция камеры корректируется, чтобы следить за персонажем игрока.
        Отображаются элементы пользовательского интерфейса, такие как здоровье и собранные предметы.
        Через объект `message_manager` отображаются и обновляются игровые сообщения.
        Если здоровье игрока упадёт до нуля, предоставляется возможность перезапустить уровень с помощью клавиши `R`.
        Игра завершается, когда появляется сообщение с конкретным префиксом.
        Локальные переменные
        - `scroll_x`: int Горизонтальное смещение камеры относительно игрока.
        - `scroll_y`: int Вертикальное смещение камеры относительно игрока.
        - `level`: Level Инициированный объект уровняс заданными параметрами для генерации геометрии и интерактивности.
        - `UI_textures`: dict Словарь, содержащий текстуры для интерфейса пользователя, в данном случае здоровье и рыбу, масштабированные до подходящего размера.
"""


scroll_x = 0  # Camera
scroll_y = 0

level = Level(sc, rsc.texture_symbols, [-200, -400])

pg.mixer.music.play(-1)

UI_textures = {"hp": pg.transform.scale(pg.image.load("heart.png"), (50, 50)),
               "fish": pg.transform.scale(pg.image.load("fish.png"), (50, 50))}

message_manager = Message(main_font, [WIDTH // 2, HEIGHT - 100], sc)

while True:
    delta_time = clock.tick(FPS)
    player.hp -= delta_time * 0.0008
    sc.fill((200, 200, 200))
    sc.blit(rsc.background[1], (WIDTH - scroll_x / 500, -scroll_y / 500))
    sc.blit(rsc.background[1], (-scroll_x / 500, -scroll_y / 500))
    sc.blit(rsc.background[1], (-scroll_x / 500, -scroll_y / 500))

    sc.blit(rsc.background[2], (WIDTH - scroll_x / 40, 80 - scroll_y / 40))
    sc.blit(rsc.background[2], (-scroll_x / 40, 80 - scroll_y / 40))
    sc.blit(rsc.background[2], (-scroll_x / 40, 80 - scroll_y / 40))

    sc.blit(rsc.background[0], (WIDTH - scroll_x / 4, 10 - scroll_y / 4))
    sc.blit(rsc.background[0], (-scroll_x / 4, 10 - scroll_y / 4))
    sc.blit(rsc.background[0], (-scroll_x / 4, 10 - scroll_y / 4))

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            exit()
    player_data = player.update(delta_time, level.update(scroll=[scroll_x, scroll_y]), (scroll_x, scroll_y))
    player.draw()
    # Camera
    if player.rect.x - scroll_x != 0:
        scroll_x += (player.rect.x - scroll_x - (WIDTH / 2)) / 7

    if player.rect.y - scroll_y != 0:
        scroll_y += (player.rect.y - scroll_y - (HEIGHT / 2)) / 7

    # UI
    sc.blit(UI_textures["hp"], (20, HEIGHT - 640))
    sc.blit(main_font.render(str(int(player.hp)), True, (0, 0, 0)), (90, HEIGHT - 625))

    sc.blit(UI_textures["fish"], (20, HEIGHT - 540))
    sc.blit(main_font.render(str(int(player.collected_fish)), True, (0, 0, 0)), (90, HEIGHT - 525))
    message_manager.update(delta_time)
    if "message" in player_data:
        message_manager.show_message(player_data["message"][0], player_data["message"][1])
    if player.hp <= 0:
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            level.start()
    if "message_1" in player_data:
        message_manager.show_message(player_data["message_1"][0], player_data["message_1"][1])
        pg.quit()

    pg.display.update()
main_menu()
