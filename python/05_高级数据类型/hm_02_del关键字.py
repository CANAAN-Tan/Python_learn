name_list = ["张三","李四","王五","王小二"]

# 使用del关键字(delete)删除列表元素
# 日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del关键字本质上是用来将一个变量从内存中删除的
name = "小明"

del name

print(name_list)