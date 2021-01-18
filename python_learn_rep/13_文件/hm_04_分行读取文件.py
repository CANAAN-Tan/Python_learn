file = open("README")

while True:
    text = file.readline()

    # 判断是否读取到内容,没有读取到内容就退出循环
    if not text:
        break

    print(text)

file.close()