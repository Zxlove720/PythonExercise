import numpy as np


# 202358234044 吴振博
# 1. 创建一个对角矩阵，并返回该矩阵中元素的数量。
# 导入模块 numpy，计算表达式 numpy.diag((1,2,3,4)) 的值，以及 numpy.diag((1,2,3,4)).size 的值。
def task1():
    diag_matrix = np.diag((1, 2, 3, 4))
    print("对角矩阵:\n", diag_matrix)
    element_count = np.diag((1, 2, 3, 4)).size
    print("元素数量:", element_count)


# 202358234044 吴振博
# 2. 获取一个数组的形状。
# 导入模块 numpy，计算表达式 numpy.array((1,2,3,4)).shape 的值，以及 numpy.array([[ 1,2,3,4,5],[ 6,7,8,9,10]]).shape 的值。
def task2():
    array1 = np.array((1, 2, 3, 4))
    print("数组 array1 的形状:", array1.shape)
    array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("数组 array2 的形状:", array2.shape)


# 202358234044 吴振博
# 3. 改变数组的大小。
# a = numpy.arange(1,11,1)，改为 2 行 5 列。
def task3():
    a = np.arange(1, 11, 1)
    resized_a = a.reshape(2, 5)
    print("改变大小后的数组:\n", resized_a)


# 202354 吴振博
# 4. 数组与数组的运算。
# a = numpy.array((1,2,3))， b = numpy.array(([1,2,3], [4,5,6], [7,8,9]))，c = a * b，分别求 c，c/b，c/a，a+a,a*a,a-a,a/a,a+b 的值。
def task4():
    a = np.array((1, 2, 3))
    b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    c = a * b
    print("c = a * b 的结果:\n", c)
    print("c / b 的结果:\n", c / b)
    print("c / a 的结果:\n", c / a)
    print("a + a 的结果:", a + a)
    print("a * a 的结果:", a * a)
    print("a - a 的结果:", a - a)
    print("a / a 的结果:", a / a)
    print("a + b 的结果:\n", a + b)


# 202358234044 吴振博
# 5. 数组转置的运算。
# a = numpy.array((1,2,3,4)),b = numpy.array(([1,2,3], [4,5,6], [7,8,9])),分别求 a 和 b 的转置。
def task5():
    a = np.array((1, 2, 3, 4))
    b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    print("a 的转置:", a.T)
    print("b 的转置:\n", b.T)


# 202358234044 吴振博
# 6. 对数据进行排序。
# x = numpy.array([3,1,2,4])，返回排序后元素的原下标，获取排序后的元素，获取最大值和最小值的下标。
def task6():
    x = np.array([3, 1, 2, 4])
    sorted_index = np.argsort(x)
    print("排序后元素的原下标:", sorted_index)
    sorted_x = np.sort(x)
    print("排序后的元素:", sorted_x)
    max_index = np.argmax(x)
    min_index = np.argmin(x)
    print("最大值的下标:", max_index)
    print("最小值的下标:", min_index)


# 202358234044 吴振博
# 7. 数组元素访问。
# b = numpy.array(([1,2,3],[4,5,6],[7,8,9]))，分别获取数组第 0 行，第 0 行第 2 列的元素值，第 0 行和第 1 行，第 0 行第 1 列的元素和第 0 行第 2 列的元素。
def task7():
    b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
    print("数组 b 的第 0 行:", b[0])
    print("数组 b 的第 0 行第 2 列元素:", b[0, 2])
    print("数组 b 的第 0 行和第 1 行:\n", b[:2])
    print("数组 b 的第 0 行第 1 列元素和第 0 行第 2 列元素:", b[0, 1], b[0, 2])


# 202358234044 吴振博
# 8. 数组切片操作。
# a = numpy.arange(10)，分别对其反向切片， 隔一个取一个元素，取前 5 个元素。
def task8():
    a = np.arange(10)
    print("数组 a 的反向切片:", a[::-1])
    print("数组 a 隔一个取一个元素:", a[::2])
    print("数组 a 的前 5 个元素:", a[:5])


# 202358234044 吴振博
# 9. 布尔运算。
# x = numpy.random.rand(10)，比较数组 x 中每个元素值是否大于 0.5，获取数组 x 中大于 0.5 的元素，测试数组 x 是否全部元素都小于 1。
def task9():
    x = np.random.rand(10)
    print("数组 x 中元素是否大于 0.5 的比较结果:", x > 0.5)
    print("数组 x 中大于 0.5 的元素:", x[x > 0.5])
    print("数组 x 是否全部元素都小于 1:", np.all(x < 1))


# 202358234044 吴振博
# 10. 生成一个包含从 0-10 的数组。
def task10():
    array_0_10 = np.arange(11)
    print("从 0 到 10 的数组:", array_0_10)


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    task10()