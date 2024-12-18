# # python 列表
#
# # 创建
# my_list1 = [1,2,3,4,5]
# # list方法可以创建一个列表，但是其参数需要一个可迭代对象
# my_list2 = list(range(6))
# my_list3 = list((1,2,3,4,5,6))
#
# # 遍历
# for i in my_list1:
#     print(i, end=" ")
# print()
#
# # 遍历二维列表
# my_list4 = [[1,2,3,4,5], [6,7,8,9,10]]
# for i in my_list4:
#     for j in i:
#         print(j, end=" ")
#     print()
#
# # 添加
# my_list1.append(6)
# print(my_list1)
#
# # 添加多个
# my_list1.extend(range(5))
# print(my_list1)
#
# my_list1 = [1,2,3,4,5]
# # 插入
# my_list1.insert(1, 0)
# print(my_list1)
#
# # 删除
# del my_list1[1]
# print(my_list1)
#
# # # del 可以直接将这个列表整个删除（不是清除）
# # del my_list1
# # print(my_list1)
#
# # pop就是将元素从列表中拿出来，自然也就删除了元素
# number = my_list1.pop(1)
# print(number)
# print(my_list1)
#
# # remove 删除第一次出现的元素
# my_list1.remove(1)
# print(my_list1)
#
# # clear 清空列表
# my_list1.clear()
# print(my_list1)
#
# mylist1 = [1,2,3,4,5,6]
# # 统计某元素出现的次数
# count = mylist1.count(1)
# print(count)
# # 查找某元素的下标
# index = mylist1.index(5)
# print(index)
# # 查看容器内的元素个数（其实也就是该容器的长度）
# length = len(mylist1)
# print(length)
from operator import index

my_list = [21,25,21,23,22,20]
print(my_list)

my_list.append(31)
print(my_list)

my_list.extend([29,33,30])
print(my_list)

first_element = my_list[0]
print(first_element)
print(my_list)

last_element = my_list.pop(-1)
print(last_element)
print(my_list)

index = my_list.index(31)
print(index)

