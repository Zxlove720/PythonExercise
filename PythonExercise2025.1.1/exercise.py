# my_list = ["heima", "chengxuyuan", "java"]
# my_set = set(my_list)
# print(my_list)
# for i in my_list:
#     print(i)
# print(f"my_set的内容是{my_set}，其类型是{type(my_set)}")
#
# my_set2 = set(my_list)
# print(my_set.difference(my_set2))
# print(my_set)
# print(my_set2)
# print(my_set.difference_update(my_set2))
# print(my_set)
# print(my_set2)


my_dic = {"apple":8, "pear":5, "watermelon":2, "milk":3, "meat":12}
for i in my_dic:
    # 对dic进行遍历，取出的是每一个键；并非是键值对
    print(i)
    # 通过[键]，可以从dic中取得值
    print(my_dic[i])

print(type(my_dic.keys()))

# 字典嵌套
my_dic2 = {
    "张三": {
        "语文": 120,
        "数学": 120,
        "英语": 120
    },
    "李四": {
        "语文": 110,
        "数学": 110,
        "英语": 110
    },
    "王五": {
        "语文": 100,
        "数学": 100,
        "英语": 100
    }
}

# 可以通过键的嵌套获取出嵌套字典中的值
print("___________________________________________")
print(my_dic2["张三"]["语文"])

# 通过for循环遍历嵌套字典
print(my_dic2)
for i in my_dic2:
    print(i, end=": ")
    score = my_dic2[i]
    for subject in score:
        print(subject, end=": ")
        print(score[subject], end=" ")
    print()



