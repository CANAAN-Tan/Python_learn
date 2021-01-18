class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫得跟神一样...")

xtq = XiaoTianQuan()

# 如果子类中，重写了父类的方法
# 调用的方法以子类新重写的方法为准
xtq.bark()