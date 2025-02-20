import pygame


# 左上角默认为(0,0),将游戏的资源分配给ship类,使得能够使用屏幕资源
class Ship:
    def __init__(self, ai_game):
        # 初始化飞船
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()  # pygame 将所有元素默认为矩形
        # 加载飞船
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        # 飞船默认放置在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):  # 绘制功能
        self.screen.blit(self.image, self.rect)  # 指定位置绘制飞船
