import pygame
import pygame as pg
import sys
from knopka import ImageKnopka
from player import Player
from config import *
from level import Level
from resources import Resources

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
main_background = pg.image.load("back1.jpg")
pg.display.set_caption("Cut cat")
clock = pg.time.Clock()
FPS = 60

pg.mixer.music.load("meoww.mp3")
player = Player(sc, Resources.player_image_r, Resources.player_image_l)




def main_menu():
    lapa = ImageKnopka(WIDTH / 2 - (190 / 2), 200, 200, 150, "", "lapa.png", "lapa1.png", "meow.mp3")
    door = ImageKnopka(WIDTH / 2 - (125 / 2), 350, 100, 100, "", "door.png", "door1.png", "meow.mp3")
    running = True
    while running:
        sc.fill((0, 0, 0))
        sc.blit(main_background, (0, 0))
        font = pygame.font.SysFont('Bauhaus 93', 70)
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
    scroll_x = 0 # Camera
    scroll_y = 0
    level = Level(sc, Resources.textures, [-100, -800])
    pg.mixer.music.play(-1)
    while True:
        delta_time = clock.tick(FPS)
        sc.fill((200, 200, 200))
        sc.blit(Resources.background[1], (-scroll_x / 300, -scroll_y / 300))

        sc.blit(Resources.background[2], (-scroll_x / 40, -scroll_y / 40))

        sc.blit(Resources.background[0], (-scroll_x / 4, -scroll_y / 4))


        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit()
        player.update(delta_time, level.update(scroll=[scroll_x, scroll_y]), (scroll_x, scroll_y))
        player.draw()

        if player.rect.x - scroll_x != 0:
            scroll_x += (player.rect.x - scroll_x - (WIDTH/2))/7

        if player.rect.y - scroll_y != 0:
            scroll_y += (player.rect.y - scroll_y - (HEIGHT/2))/7


        pg.display.update()
new_game()


