# 3.5 在游戏循环中监听事件
# 事件event
# 就是游戏启动后，用户针对游戏所做的操作
# 例如点击关闭按钮，点击鼠标，按下键盘等等
#
# 监听：
# 在游戏中，判断用户具体的操作
# 只有捕获到用户具体的操作，才能有针对性的做出响应
#
# 代码实现：
# pygame中通过pygame.event.get()可以获得用户当前所做动作的事件列表
#     用户可以同一事件做很多事情
# tips：这段代码非常固定，几乎所有的pygame游戏都大同小异

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

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    # 2. 修改飞机的位置，坐标每秒移动多少像素。
    hero_rect.y -= 1

    # 判断飞机的位置，一旦y<=0则移动飞机到底部
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()


pygame.quit()