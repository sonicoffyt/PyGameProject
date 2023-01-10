from menu import *


class Window:
    """Класс инициализации всех окон"""
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1400, 900
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.helping = HelpMenu(self)
        self.game_over = GameOver(self)
        self.difficulty = Difficulty(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        """Запускает цикл игры"""
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        """Проверяет  нажатия/закрытие окон"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open('./data/data.txt', 'w')
                f.write('0')
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        """Обновление нажатий"""
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        """Чтобы не париться с выводом текста"""
        font = pygame.font.Font("data/Dited.otf", size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
