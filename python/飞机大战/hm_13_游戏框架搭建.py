"""游戏框架搭建

目标 -- 使用面向对象涉及飞机大战游戏类（设计游戏逻辑）
    1、明确主程序职责
    2、实现主程序类
    3、准备游戏精灵组

01.明确主程序职责：
回顾快速入门案例，一个游戏主程序的职责可以分为两个部分
    游戏初始化
    游戏循环

根据明确的职责，设计PlaneGame类如下：
PlaneGame类：
    属性：
        1、screen
        2、clock
        3、精灵组或精灵
    方法：（__打头的为私有方法）
        1、__init__(self):
        2、__creat_sprites(self):
        游戏初始化要做的事：
        设置游戏窗口
        创建游戏时钟
        创建精灵、精灵组

        3、start_game(self):
        4、__event_handler(self):
        5、__check_collide(self):
        6、__update_sprite(self):
        7、__game_over():
        游戏循环要做的事：
        设置刷新频率
        事件监听
        碰撞检测
        更新/绘制精灵组
        更新屏幕显示

02.实现飞机大战主游戏类

2.1 明确文件职责
plane_main                plane_sprites
游戏主程序       <---    屏幕尺寸常量游戏精灵子类等

plane_main职责
    1、封装主游戏类
    2、创建游戏对象
    3、启动游戏

plane_sprites
    1、封装游戏中所有需要使用的精灵子类
    2、提供游戏的相关工具 """

