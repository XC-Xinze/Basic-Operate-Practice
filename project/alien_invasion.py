import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        #       self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("AlienInvasion")
        self.bg_color = (230, 230, 230)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)

    def run_game(self):
        while True:
            # 侦听键盘
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()  # 使最近绘制的屏幕可见
            self.clock.tick(60)  # tick 参数接受的参数为 帧率


if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
