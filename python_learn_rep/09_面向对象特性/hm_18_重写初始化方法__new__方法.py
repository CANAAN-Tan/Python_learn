class MusicPlayer(object):

    # *多值的元组参数，**多值的字典参数
    def __new__(cls, *args, **kwargs):

        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间
        # 使用super()调用父类方法，并记录
        instance = super().__new__(cls)

        # 3. 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")

# 创建播放器对象
player = MusicPlayer()

print(player)