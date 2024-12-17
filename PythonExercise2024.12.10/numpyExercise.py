import numpy as np

# # 202358234044 吴振博
# diagonal_matrix = np.diag((1, 2, 3, 4))
# print("对角矩阵为：")
# print(diagonal_matrix)
#
# element_count = diagonal_matrix.size
# print("对角矩阵中元素的数量为：", element_count)

# # 202358234044 吴振博
# import numpy as np
# # 创建一维数组
# one_d_array = np.array((1, 2, 3, 4))
# print("一维数组的形状为：")
# print(one_d_array.shape)
#
# # 创建二维数组
# two_d_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print("二维数组的形状为：")
# print(two_d_array.shape)

# # 202358234044 吴振博
#
# a = np.arange(1, 11, 1)
# print("原始数组 a：")
# print(a)
#
# # 将数组 a 改变为 2 行 5 列的数组
# a_reshaped = a.reshape(2, 5)
# print("改变大小后的数组 a：")
# print(a_reshaped)


# # 202358234044 吴振博
# # 创建数组 a
# a = np.array((1, 2, 3))
# print("数组 a:")
# print(a)
#
# # 创建数组 b
# b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print("数组 b:")
# print(b)
#
# # 计算 c = a * b
# c = a * b
# print("c = a * b 的结果:")
# print(c)
#
# # 计算 c / b
# print("c / b 的结果:")
# print(c / b)
#
# # 计算 c / a
# print("c / a 的结果:")
# print(c / a)
#
# # 计算 a + a
# print("a + a 的结果:")
# print(a + a)
#
# # 计算 a * a
# print("a * a 的结果:")
# print(a * a)
#
# # 计算 a - a
# print("a - a 的结果:")
# print(a - a)
#
#
#
# # 计算 a / a
# print("a / a 的结果:")
# print(a / a)
#
# # 计算 a + b
# print("a + b 的结果:")
# print(a + b)


# 202358234044 吴振博
# # 创建数组 a
# a = np.array((1, 2, 3, 4))
# print("数组 a:")
# print(a)
# # 求数组 a 的转置
# a_transpose = a.T
# print("数组 a 的转置:")
# print(a_transpose)
#
# # 创建数组 b
# b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print("数组 b:")
# print(b)
# # 求数组 b 的转置
# b_transpose = b.T
# print("数组 b 的转置:")
# print(b_transpose)


# # 202358234044 吴振博
# x = np.array([3, 1, 2, 4])
# print("原始数组 x:")
# print(x)
#
# sorted_index = np.argsort(x)
# print("排序后元素的原下标:")
# print(sorted_index)
#
# sorted_x = np.sort(x)
# print("排序后的元素:")
# print(sorted_x)
#
# max_index = np.argmax(x)
# print("最大值的下标:")
# print(max_index)
#
# min_index = np.argmin(x)
# print("最小值的下标:")
# print(min_index)

# # 202358234044 吴振博
# # 创建数组 b
# b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
# print("数组 b:")
# print(b)
#
# # 获取数组第 0 行
# row_0 = b[0]
# print("数组第 0 行:")
# print(row_0)
#
# # 获取数组第 0 行第 2 列的元素值
# element_0_2 = b[0, 2]
# print("数组第 0 行第 2 列的元素值:")
# print(element_0_2)
#
# # 获取数组第 0 行和第 1 行
# rows_0_1 = b[0:2]
# print("数组第 0 行和第 1 行:")
# print(rows_0_1)
#
# # 获取数组第 0 行第 1 列的元素和第 0 行第 2 列的元素
# elements_0_1_0_2 = b[0, 1:3]
# print("数组第 0 行第 1 列的元素和第 0 行第 2 列的元素:")
# print(elements_0_1_0_2)


# # 202358234044 吴振博
# # 创建一个从 0 到 9 的数组 a
# a = np.arange(10)
# print("原始数组 a:")
# print(a)
#
# # 对数组 a 进行反向切片
# reverse_slice = a[::-1]
# print("反向切片后的数组:")
# print(reverse_slice)
#
# # 隔一个取一个元素
# every_other_element = a[::2]
# print("隔一个取一个元素的数组:")
# print(every_other_element)
#
# # 取前 5 个元素
# first_five_elements = a[:5]
# print("取前 5 个元素的数组:")
# print(first_five_elements)


# # 202358234044 吴振博
# # 创建一个包含 10 个随机数的数组 x
# x = np.random.rand(10)
# print("数组 x:")
# print(x)
#
# # 比较数组 x 中每个元素值是否大于 0.5
# greater_than_0_5 = x > 0.5
# print("数组 x 中每个元素是否大于 0.5:")
# print(greater_than_0_5)
#
# # 获取数组 x 中大于 0.5 的元素
# elements_greater_than_0_5 = x[x > 0.5]
# print("数组 x 中大于 0.5 的元素:")
# print(elements_greater_than_0_5)
#
# # 测试数组 x 是否全部元素都小于 1
# all_less_than_1 = np.all(x < 1)
# print("数组 x 是否全部元素都小于 1:")
# print(all_less_than_1)

# 202358234044 吴振博
# 生成一个包含从 0 到 10 的数组
array_0_to_10 = np.arange(0, 11 )
print("包含从 0 到 10 的数组:")
print(array_0_to_10)

