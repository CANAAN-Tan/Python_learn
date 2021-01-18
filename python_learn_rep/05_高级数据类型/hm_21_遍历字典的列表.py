students = [
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学院列表中指定的姓名
find_name = "李四"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了 %s " % find_name)

        # 如果找到了，应直接退出循环，而不再遍历后续元素
        break
#    else:
#       print("抱歉没有找到 %s " % find_name)
else:
   print("抱歉没有找到 %s " % find_name)
print("循环结束")
