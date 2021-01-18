class A:

    def test(self):
        print("A --- test 方法")

    def demo(self):
        print ("A --- demo 方法")

class B:

    def test(self):
        print("B --- test 方法")

    def demo(self):
        print("B --- demo 方法")

class C(B,A):
    """多继承可以让子类对象，同事具有多个父类的属性和方法"""
    """尽量避免多继承，或者多个类有同名属性或方法"""
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序
print()

# 确定C类对象调用方法的顺序
print(C.__mro__)