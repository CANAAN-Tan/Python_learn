# 3.4 英雄的简单动画实现
# 需求：
# 1、在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
# 2、在游戏循环中每次让英雄的y-1 --- 向上移动
# 3、y <= 0将英雄移动到屏幕的底部
#
# 提示：
# 每一次调用update（）方法之前，需要把所有的游戏图像都重新绘制一遍
# 而且应该最先重新绘制背景图像
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

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 300, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)   # 每秒执行几次内部代码

    # 2. 修改飞机的位置，坐标每秒移动多少像素。
    hero_rect.y -= 1

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()


pygame.quit()