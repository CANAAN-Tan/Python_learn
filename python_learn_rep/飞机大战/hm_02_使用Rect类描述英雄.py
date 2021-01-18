# Rect类
# Rect类是pygame专门提供的类用于描述矩形区域

# Rect(x, y, ,size, width, height)
# size属性是一个元组属性，返回的第一个值是width，第二个值是height

# tips:pygame.Rect是一个特殊类，内部只是封装了一些数字计算不执行pygame.init（）方法同样能够直接使用

# 导入包
import pygame

# 定义英雄其实原点坐标为（100,500），英雄尺寸为宽度120，高度125
hero_rect = pygame.Rect(100, 500, 120,125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width,hero_rect.height))
print("%d %d" % hero_rect.size)