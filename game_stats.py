class GameStats:
    def __init__(self, game):
        self.score = 0
        self.ships_left = None
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
