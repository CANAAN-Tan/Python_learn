"""4 理解精灵和精灵组
4.1 精灵和精灵组
在刚完成的案例中，图像加载、位置变化、绘制图像都需要程序猿编写代码分别处理
如果遇到要批量操作同类型对象时，为了简化开发步骤，pygame提供了两个类：
精灵类：pygame.sprite.Sprite
存储图像数据image和位置rect的对象
精灵组：pygame.sprite.Group
多个精灵组成的列表

精灵：（需要派生子类）
属性image：记录图像数据
属性rect：记录在屏幕上的位置
方法update(*args)：更新精灵位置
方法kill():从所有组中删除

精灵组：
初始化方法__init__(self, *精灵):
方法add(*sprites):向组中增加精灵
方法sprites():返回所有精灵列表
方法update(*args):让组中所有精灵调用update方法
方法draw(Surface):将组中所有精灵的image，会知道Surface的rect位置

代码结构：
游戏初始化：
1、创建精灵
2、创建精灵组

游戏循环：
1、精灵组.update()
2、精灵组.draw(screen)
3、pygame.display.update()

4.3 使用游戏精灵和精灵组创建敌机
需求：
使用刚刚派生的游戏精灵和精灵组创建敌机，并且实现敌机动画
步骤:
1、使用from导入plane_sprites模块
    from导入的模块可以直接使用
    import导入的模块需要通过模块名.来使用
2、字啊游戏初始化创建精灵对象和精灵组对象
3、在游戏循环中让精灵组分别调用update()和draw(screen)方法

职责：
精灵：
    封装图像image、位置rect和速度speed
    提供update()方法，根据游戏需求，更新位置rect

精灵组：
    包含多个精灵对象
    udate()方法，让精灵组中的所有精灵调用update()方法更新位置
    draw(screen)方法，在screen上绘制精灵组中的所有精灵  """

import pygame
from plane_sprites import *

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

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)   # 每秒执行几次内部代码

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # 调用quit方法卸载所有的模块
            pygame.quit()

            # 调用exit方法退出系统，直接终止当前正在执行的程序
            exit()

    # 2. 修改飞机的位置，坐标每秒移动多少像素。
    hero_rect.y -= 1

    # 判断飞机的位置，一旦y<=0则移动飞机到底部
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中的所有精灵更新位置
    enemy_group.update()
    # draw - 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4. 调用update方法更新显示
    pygame.display.update()

pygame.quit()