# 3.理解游戏循环和游戏时钟
#
# 3.1 游戏中的动画实现原理
# * 跟电影的原理类似，游戏中的动画效果本质上是快速的在屏幕上绘制图像
#     电影是将多张静止的电影胶片连续快速的播放，产生连贯的视觉效果
# * 一般在电脑上每秒绘制60次，就能够达到非常连续高品质的动画效果
#     每次绘制的结果被称为帧 Frame

# 3.2 游戏初始化要做的事：
# 1、设置游戏窗口
# 2、绘制图像初始位置
# 3、设置游戏时钟
#
# 游戏循环要做的事：
# 1、设置刷新帧率
# 2、检测用户交互
# 3、更新所有图像位置
# 4、更新屏幕显示

# 3.3 游戏时钟
# pygame专门提供了一个类pygame.time.Clock可以方便的设置屏幕绘制速度--刷新帧率
# 要使用时钟对象需要两步：
# 1、在游戏初始化时创建一个是时钟对象
# 2、在游戏循环中让时钟对象调用tick(帧率)方法
# tick方法会根据上次被调用的时间，自动设置游戏循环中的延时


import pygame

# 游戏的初始化
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

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏的正式开始！
i = 0

while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(1)   # 每秒执行几次内部代码
    print(i)

    i += 1

    pass

pygame.quit()