hello_str = "hello world"

# 1 判断是否以指定字符串开始
print((hello_str.startswith("hell")))

# 2 判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3 查找指定字符串的位置
# index同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4 替换字符换
print(hello_str.replace("world", "python"))
print(hello_str) 