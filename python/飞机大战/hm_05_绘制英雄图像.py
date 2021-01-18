# 需求：
# 1、加载me1.png创建英雄飞机
# 2、将英雄飞机绘制在屏幕的(200,500)位置
# 3、调用屏幕更新显示图像

import pygame

pygame.init()

# 创建游戏的窗口
# 记录返回的游戏窗口屏幕
# 同时制定游戏窗口的尺寸（根据背景图的像素）
screen = pygame.display.set_mode((480, 600))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit方法绘制图像
screen.blit(bg, (0, 0))
# 3> update方法更新屏幕显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 600))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()