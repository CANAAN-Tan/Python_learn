name_list = ["zhangsan","lisi","wangwu"]

# 1 取值和取索引
# 不可超出索引范围
print((name_list[2]))

# 知道内容，确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不再列表中，程序会报错
print(name_list.index("wangwu"))

# 2 修改
name_list[1] = "李四"
# 列表指定的索引超出范围，程序会报错
# name_list[3] = "王小二"

# 3 增加
name_list.append("王小二")
# insert方法可以在列表中指定索引位置插入数据
name_list.insert(1, "小妹儿")

# extend方法可以吧其他列表中的完整内容追加到当前列表的末尾
temp_list = ["孙悟空","猪二哥","沙师弟"]
name_list.extend(temp_list)

# 4 删除
# remove方法可以从列表中删除指定数据
name_list.remove("wangwu")
# pop方法默认删除列表最后的数据，也可指定删除数据的索引号
name_list.pop(1)
# clear方法可将列表所有数据删除
name_list.clear()


print(name_list)