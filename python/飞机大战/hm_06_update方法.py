# 理解update()方法的作用
# 可以在screen对象完成所有blit方法之后，统一调用一次display.update方法，同样可以在屏幕上看到最终的绘制结果
#
# 1、使用display.set_mode()创建的screen对象是一个内存中屏幕数据的对象，可以理解成是油画的画布
# 2、screen.blit方法可以在画布上绘制很多图像
# 例如英雄、敌机、子弹。。。
# 这些图像有可能会彼此重叠或覆盖
# 3、display.update()方法会将画布的最终结果绘制在屏幕上，这样可以提高屏幕绘制效率，增加游戏的流畅度

import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 600))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 600))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()