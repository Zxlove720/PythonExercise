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