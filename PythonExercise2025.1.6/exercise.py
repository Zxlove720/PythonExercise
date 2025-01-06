# 素数判断

# def check_number(number):
#     key = 2
#     while key < number:
#         if number % key == 0:
#             return False
#         key += 1
#     return True
#
# if __name__ == '__main__':
#     for i in range(2, 100):
#         if check_number(i):
#             print(i)

# 斐波那契
# def feibo(n: int):
#     my_list = [1, 1]
#     for i in range(2, n):
#         my_list.append(my_list[i - 1] + my_list[i - 2])
#     print(my_list)
#
# if __name__ == '__main__':
#     n: int = int(input("请输入你想要几个斐波那契数"))
#     feibo(n)

# 水仙花
# def check_number(n:int):
#     temp = n
#     i = 0
#     my_list = []
#     while n > 0:
#         i += 1
#         my_list.append(n % 10)
#         # python中的/不是整除，会保留小数部分，//才是整除
#         n //= 10
#     count = 0
#     for e in my_list:
#         count += e ** i
#     if count == temp:
#         return True
#     return False
#
# if __name__ == '__main__':
#     n:int = int(input("请输入一个数字\n"))
#     if check_number(n):
#         print(f"{n}是水仙花数")
#     else:
#         print(f"{n}不是水仙花数")

# a + aa + aaa
def get_sum(a:int, n:int):
    temp = a
    count = a
    for i in range(1, n):
        a = a * 10 + temp
        count += a
    return count

if __name__ == '__main__':
    # number:int = int(input("请输入想要加的数字"))
    # n:int = int(input("请输入想要加的次数"))
    # result = get_sum(number, n)
    # print(result)

    a = input()
    for i in range(2, 13, 2):
        

