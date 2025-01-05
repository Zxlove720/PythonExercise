# 文件写入操作
import time

# with open("E:/wzb.txt", "w", encoding="UTF-8") as f:
#     f.write("hello world")
#     f.flush()
#     # close方法中其实是内置了flush方法的功能的

# 拷贝一个文件
with open("E:/wzb.txt", "r", encoding="UTF-8") as f:
    with open("E:/wzb_copy.txt", "w", encoding="UTF-8") as c:
        for line in f:
            c.write(line)
