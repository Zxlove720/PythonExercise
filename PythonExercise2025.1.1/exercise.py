my_list = ["heima", "chengxuyuan", "java"]
my_set = set(my_list)
print(my_list)
for i in my_list:
    print(i)
print(f"my_set的内容是{my_set}，其类型是{type(my_set)}")

my_set2 = set(my_list)
print(my_set.difference(my_set2))
print(my_set)
print(my_set2)
print(my_set.difference_update(my_set2))
print(my_set)
print(my_set2)
