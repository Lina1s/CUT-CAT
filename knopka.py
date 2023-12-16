import pygame


class ImageKnopka:
    """
    Класс кнопки с изображением для приложений на Pygame, с возможностью изменения изображения при наведении и воспроизведением звуковых эффектов.

    :param x: X-координата верхнего левого угла кнопки.
    :param y: Y-координата верхнего левого угла кнопки.
    :param width: Ширина кнопки.
    :param height: Высота кнопки.
    :param text: Текст, отображаемый на кнопке.
    :param image_path: Путь к файлу изображения для кнопки.
    :param hover_image_path: Путь к файлу изображения для кнопки при наведении курсора (необязательный параметр).
    :param sound_path: Путь к файлу звукового эффекта, воспроизводимого при клике по кнопке (необязательный параметр).

    Пример использования::

        play_button = ImageKnopka(100, 100, 200, 50, "Играть", "button.png", "button_hover.png", "click.wav")

    .. method:: __init__(x, y, width, height, text, image_path, hover_image_path=None, sound_path=None)

        Инициализация экземпляра ImageKnopka с заданными параметрами. Создаёт изображения для кнопки и звук, а также формирует прямоугольник для обработки событий столкновения.

    .. method:: draw(screen)

        Отрисовывает кнопку на указанной Pygame поверхности экрана. При наведении курсора использует изображение для наведения, отображает текст кнопки, центрированный относительно её.

        :param screen: Поверхность экрана Pygame, на которой будет отрисована кнопка.

    .. method:: check_hover(mouse_pos)

        Обновляет статус наведения курсора на кнопку в зависимости от позиции мыши.

        :param mouse_pos: Кортеж (x, y) с текущей позицией курсора мыши.

    .. method:: handle_event(event)

        Реагирует на события мыши. В частности, при нажатии левой кнопкой мыши с наведением на кнопку воспроизводит связанный с ней звуковой эффект (если таковой имеется) и размещает в очереди событий Pygame пользовательское событие USEREVENT, указывающее на клик по кнопке.

        :param event: Объект события Pygame для обработки.

    .. attribute:: x

        X-координата верхнего левого угла кнопки.

    .. attribute:: y

        Y-координата верхнего левого угла кнопки.

    .. attribute:: width

        Ширина кнопки.

    .. attribute:: height

        Высота кнопки.

    .. attribute:: text

        Текст, отображаемый на кнопке.

    .. attribute:: image

        Изображение кнопки по умолчанию.

    .. attribute:: hover_image

        Изображение кнопки при наведении курсора.

    .. attribute:: rect

        Прямоугольник Pygame, представляющий область кнопки для обнаружения столкновений и отрисовки.

    .. attribute:: sound

        Объект звукового эффекта Pygame mixer, который воспроизводится при нажатии на кнопку.

    .. attribute:: is_hovered

        Булево значение, показывающее, наведён ли курсор на кнопку в данный момент.

    """

    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.SysFont('Bauhaus 93', 40)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):  # проверка события нажатия левой кнопкой мыши, если да то вкл.музыку
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))  # мышка была нажата
