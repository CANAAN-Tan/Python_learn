# 创建游戏主窗口
# pygame专门提供了一个模块pygame.display用于创建、管理游戏窗口
# 方法：
# pygame.display.set_mode()
# 说明：初始化游戏显示窗口
#
# pygame.display.update()
# 说明：刷新屏幕内容显示
#
# set_mode()方法：
# set_mode(resolution=(0,0), flags=0, depth=0)  --> Surface
#
# 参数：
# resolution指定屏幕的宽和高，默认创建的窗口大小和电脑屏幕一样大
# flags指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
# depth表示颜色的位数，默认自动匹配
#
# 返回值：Surface
# 暂时理解为游戏屏幕，游戏的元素都需要被绘制到游戏的屏幕上
#
# 注意：必须使用变量记录set_mode方法的返回结果！因为后续所有的图像绘制都基于这个返回结果

import pygame

pygame.init()

# 创建游戏的窗口
# 记录返回的游戏窗口屏幕
# 同时制定游戏窗口的尺寸（根据背景图的像素）
screen = pygame.display.set_mode((480, 700))

# 游戏循环
while True:
    pass

pygame.quit()