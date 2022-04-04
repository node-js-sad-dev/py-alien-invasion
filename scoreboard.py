import pygame.font


class Scoreboard:
    def __init__(self, game):
        self.record_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_record()

    def prep_score(self):
        score_str = str(self.stats.score)
        print(score_str)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_record(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, self.settings.bg_color)

        self.record_rect = self.high_score_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx

        self.record_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.record_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_record()
