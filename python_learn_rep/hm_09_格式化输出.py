# 定义字符串变量 name ，输出 我的名字叫小明，请多关照！
name ="小明"
print("我的名字叫%s ， 请多关照！" % name)

# 定义整数变量student_no 输出我的学号是00001
student_no = 126565465
print("我的学号是：%05d " % student_no)

# 定义小数price、weight、money,
# 输出苹果单价9.00元/斤 购买5.00斤，
# 需支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元/斤，购买了 %.3f 斤，需支付 %.4f 元" % (price,weight,money))

# 定义一个小数scale,输出数据比例是10.00%
scale = 0.25 * 100
print("数据比例是 %.2f%%" % (scale * 10))