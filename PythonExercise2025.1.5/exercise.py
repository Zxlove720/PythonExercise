def create_new_dic():
    temp_dic = {"张三": 18, "李四": 19, "王五": 20}
    return temp_dic


if __name__ == '__main__':
    # my_dic = create_new_dic()
    # # print(my_dic)
    # # print(my_dic["张三"])
    # # # 假如键不存在，添加一个键；假如键存在，则修改其值
    # # # 原理：字典的键是唯一的
    # # my_dic["赵六"] = 21
    # # my_dic["张三"] = 999
    # # print(my_dic)
    # # print(f"字典更新后的张三年龄是{my_dic['张三']:.2f}")
    #
    # # 删除元素
    # # 通过pop方法获取指定key的value，该key被移除
    # key =  my_dic.pop("张三")
    # print(key)
    # print(my_dic)
    # # 清空
    # # clear方法直接将整个字典清空
    # my_dic.clear()
    # print(my_dic)
    # my_dic = create_new_dic()
    #
    # # keys 方法获取字典中全部的key
    # keys = my_dic.keys()
    # print(keys)
    # # 根绝获取的keys遍历字典
    # for i in keys:
    #     print(my_dic[i], end=" ")
    # print()
    # # 但其实直接遍历字典对象就是得到的其键
    # for key in my_dic:
    #     print(my_dic[key], end=" ")
    # print()
    #
    # # 其数量是键的数量
    # print(len(my_dic))

    emp = {
        "王力宏": {
            "部门": "科技部",
            "工资": 3000,
            "级别": 1
        },
        "周杰伦": {
            "部门": "市场部",
            "工资": 5000,
            "级别": 2
        },
        "林俊杰": {
            "部门": "市场部",
            "工资": 7000,
            "级别": 3
        },
        "张学友": {
            "部门": "市场部",
            "工资": 6000,
            "级别": 2
        }
    }

    # 遍历字典，给所有级别为1的员工上升一级，并+1000
    for employee in emp:
        if emp[employee]["级别"] == 1:
            emp[employee]["级别"] += 1
            emp[employee]["工资"] += 1000

    for employee in emp:
        print(employee, end=": ")
        keys = emp[employee]
        for e in keys:
            print(e, end=": ")
            print(keys[e],end=" ")
        print("")


    # 数据容器通用操作
    my_list = [1,2,3,4,5]
    # max min找最大、最小元素
    print(max(my_list))
    print(min(my_list))

    print(sorted(my_list, reverse=True))

    my_str = "abcdef"
    print(sorted(my_str, reverse=True))
