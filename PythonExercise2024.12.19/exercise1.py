# # 列表常用方法
# my_list = [1,2,3,4,5]
#
# # 增
# my_list.append(6)
# print(my_list)
#
# my_list.extend([7,8,9])
# print(my_list)
#
# # 删
# number = my_list.pop(8)
# print(f"删除了{number},现在列表内容是{my_list}")
#
# del my_list[7]
# print(my_list)
#
# # 改
# my_list[6] = 100
# print(my_list)
#
# # 查
# index = my_list.index(5)
# print(index)
#
# # 反转
# my_list.reverse()
# print(my_list)
#
# # 统计某元素的出现次数
# count = my_list.count(30)
# print(count)


# # 元组tuple
# # 元组中的内容不可变
# t = (1,2,3,4,5)
# print(t[0])
# # # 不可变，修改失败
# # t[0] = 3
# # t1 = tuple()
# # print(t1)
# print(t.index(5))
# print(t.count(5))
# print(len(t))
#
# t1 = t[1:3]
# print(t1)

# 字符串
# 字符串也是不可变的
# my_str = "hello wor ld "
# print(my_str[0])
#
# for i in my_str:
#     print(i, end=" ")
# print()
#
# # 将old全部替换为new，字符串不会改变，所以说replace方法实际上是返回了一个新的字符串
# new_str = my_str.replace(" ", "|")
# print(my_str)
# print(new_str)
#
# # 将字符串按照参数分割，然后返回一个列表
# words = my_str.split(" ")
# print(type(words))
# print(words)
#
# # 转换为大写
# upper = my_str.upper()
# print(upper)

# s = "itheima itcast boxuegu"
# print(s.count("it"))
# new_str = s.replace(" ", "|")
# print(new_str)
# lit = new_str.split("|")
# print(lit)

# 序列切片
s = "万过薪月，员序程马黑来，nohtyp学"
# 得到子串“黑马程序员”
my_list = s.split("，")
print(my_list[1][:5][::-1])

my_list2 = s.split("，")
print(my_list2[1].replace("来", "")[::-1])




