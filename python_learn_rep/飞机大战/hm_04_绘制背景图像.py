# 理解图像并实现图像绘制
#
# 在游戏中，能够看到的游戏元素大多都是图像
#     图像文件初始是保存在磁盘上的，如需使用，第一步需要加载到内存
# 要在屏幕上看到某一个图像的内容，需要三个步骤：
# 1、使用pygame.image.load()加载图像的数据
# 2、使用屏幕对象，调用blit方法将图像绘制到指定位置
# 3、调用pygame.display.update()方法更新整个屏幕的显示
#
# pygame.image        pygame.Surface      pygame.display.update()
# load(file_path)  ->  blit(图像，位置)
#
# tips:要想在屏幕上看到绘制的结果，就一定要调用pygame.display.update()方法
#
# 需求：
# 1、加载background.png创建背景
# 2、将背景绘制在屏幕的(0, 0)位置
# 3、调用屏幕更新显示背景图像

import pygame

pygame.init()

# 创建游戏的窗口
# 记录返回的游戏窗口屏幕
# 同时制定游戏窗口的尺寸（根据背景图的像素）
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")

# 2> blit方法绘制图像
screen.blit(bg, (0, 0))

# 3> update方法更新屏幕显示
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()