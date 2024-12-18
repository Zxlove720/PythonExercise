# name1 = "李四"
# name2 = "张三"
# print(name1 == name2)
#
# if name1 != "张三":
#     print("hahaha")
#
# # not关键字用于逻辑取反，相当于not后面要跟一个bool值
# if not name2 == "李四":
#     print(name2)
#
#
# # 数字母
# message = "itheima is a brand of it"
# count = 0
# for i in message:
#     if i == "a":
#         count += 1
#
# print(count)
import random

# range(number) 0-number,没有number本身
# for i in range(10):
#     print(i)
#
# # range(number1, number2) number1 - number2,没有number2
# for i in range(2, 13):
#     print(i)
#
# # range(number1, number2, step) 按照step的步长获取number1 - number2,也是不含number2的
# for i in range(2, 12, 2):
#     print(i)
#
# count = 0
# for i in range(100):
#     if i % 2 == 0:
#         count += 1
# print(count)

# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # print后面使用end=控制每一行结束后是什么，不然print函数默认换行
#         print(f"{j}*{i}={i * j:2d} ", end=" ")
#     print()


# 综合案例
money = 10000
for i in range(1, 21):
    rank = random.randint(1, 11)
    if money == 0:
        print("工资发完了，下个月再来吧")
        break
    if rank < 5:
        print(f"员工{i}，绩效为{rank}，低于5，不发工资，下一位")
        continue
    money -= 1000
    print(f"给员工{i}发了1000元工资，现在还剩{money}元工资")




