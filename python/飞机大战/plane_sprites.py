# 4.2 派生精灵子类
# 需求：
# 1、新建plane_sprites.py文件
# 2、定义GameSprite类，继承自pygame.sprite.Sprite类
#
# tips：
# 如果一个类的父类不是object，在重写初始化方法时，一定要先super()一下父类的__init__方法，以保证父类中实现的__init__代码能够被正常执行
#
# 应实现的定义对象GameSprite
# 属性：
# image   精灵图像，使用image_name加载
# rect    精灵大小，默认使用图像大小
# speed   精灵移动速度，默认为1
# 方法：
# __init__(self, image_name, speed=1):
# update(self)    每次更新屏幕时在游戏循环内调用
#     让精灵的self.rect.y += self.speed
#
# tips:
# image的get_rect()方法，可以返回pygame.Rect(0,0,图像宽,图像高)的对象

import random  # 官方模块的导入应在第三方模块导入之前
import pygame

# 屏幕大小的常量，常量按约定俗称用全大写定义
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


# 定义通用精灵类
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 重定义一下子类对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    # 重定义一些子类对象的方法
    def update(self):

        # 在屏幕的垂直方向向上移动
        self.rect.y += self.speed


# 定义背景精灵类
class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1. 调用父类方法实现精灵创建
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):  # 父类不能满足子类需求，就调用后重写部分代码

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 定义敌机精灵类
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")

        # 2. 指定敌机的初始随机速度 1 - 3
        self.speed = random.randint(1, 3)

        # 3. 指定敌机的初始随机位置
        # rect内置属性bottom,bottom = y + height
        self.rect.bottom = 0  # 让飞机从北京外面飞入

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 1. 调用父类方法，保持垂直方向的飞行
        super().update()

        # 2. 判断是否飞出屏幕，如果是，则需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    # 看销毁的飞机是否调用了__del__方法释放内存
    def __del__(self):
        pass
        # print("敌机挂了 %s" % self.rect)


# 定义英雄精灵类
class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1. 调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)

        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    # 此处不需要集成父类，因父类方法中没有定义水平移动
    def update(self):

        # 重写方法，定义英雄在水平方向的移动逻辑
        self.rect.x += self.speed
