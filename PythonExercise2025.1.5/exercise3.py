# 文件操作
# f = open("E:/测试.txt", "r", encoding="UTF-8")
# print(type(f))
#
# print(f.read())
# f.close()
# print("---------------")
# f = open("E:/测试.txt", "r", encoding="UTF-8")
# print(f.readline())
# print(f.readlines())
# f.close()
#
# print("-----------------------")
# f = open("E:/测试.txt", "r", encoding="UTF-8")
# for line in f:
#     print(line)
#
# f.close()

# 使用with open可以便捷的操作文件，with open打开的文件可以自动关闭
with open("E:/测试.txt", "r", encoding="UTF-8") as f:
    my_str = f.read()
    print(my_str)
    words = my_str.split()
    count = 0
    for e in words:
        if e == "itheima":
            count += 1
    print(count)