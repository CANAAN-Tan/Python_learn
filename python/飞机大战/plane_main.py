import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)   # 用常量代替尺寸数值(见plane_sprites)，因set_mode返回元组，所有传入size属性。
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件 - 创建敌机 1s间隔
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()  # plane_sprites中在Background类的初始化中已统一定义了路径
        bg2 = Background(True)  # plane_sprites中在Background类的初始化中用is_alt属性控制替换背景

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 指定刷新率,这里也是用在plane_sprites中定义的常量
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵
            self.__update_sprites()
            # 5、 更新显示
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            # 第一种实现向右移动方式   *** 按下抬起才算一次移动，操作灵活性低。
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")

            # 第二种实现向右移动的方式  *** 更加灵活
            # 使用键盘提供的方法获取键盘按键 - 按键元组
            # 返回所有按键的元组，如果某个键被按下，对应的值会是1
            keys_pressed = pygame.key.get_pressed()

            # 判断是否按下了方向键，判断元组中对应的按键索引值
            if keys_pressed[pygame.K_RIGHT]:
                # print("按住按键不放持续向右移动...")
                self.hero.speed = 2  # 数字为水平移动速度
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    # 因为是静态方法，所以不需要传入self且需要@staticmethod进行声明
    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':

    pygame.init()

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()