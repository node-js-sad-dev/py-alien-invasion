import pygame


class Ship:
    def __init__(self, ai_game):
        """Как параметр экран передать экран игры"""
        self.screen = ai_game.screen
        """Как параметр прямоугольника экрана передать прямоугольник экрана игры"""
        self.screen_rect = ai_game.screen.get_rect()

        """Загрузить фото корабля в игру"""
        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'), (46, 78))
        """Получить прямоугольник изображения, чтобы на экране манипулировать изображением как прямоугольником (координатами и тд)"""
        self.rect = self.image.get_rect()

        """Разместить нижний центр корабля в точке нижнего центра экрана игры"""
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
