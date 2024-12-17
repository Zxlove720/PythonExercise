# # # 202358234044 吴振博
# # from datetime import datetime
# #
# # today = datetime(2024, 11, 4)
# # start_of_year = datetime(today.year, 1, 1)
# # days = (today - start_of_year).days + 1
# # print(f"今天是今年的第{days}天。")
#
# # 202358234044 吴振博
# # total = 0
# # count = 0
# # while True:
# #     score = float(input("请输入一个分数："))
# #     total += score
# #     count += 1
# #     choice = input("是否继续输入下一个分数？（yes/no）")
# #     if choice.lower() == "no":
# #         break
# # average = total / count
# # print(f"平均分是{average}。")
# #
# #202358234044 吴振博
# # sum_value = 0
# # for i in range(1, 101):
# #     sum_value += i
# # print(sum_value)
# #
# # for num in range(1, 101):
# #     if num % 7 == 0 and num % 5!= 0:
# #         print(num, end=" ")
# # print()
# #
# #202358234044 吴振博
# # for num in range(100, 1000):
# #     hundreds_digit = num // 100
# #     tens_digit = (num // 10) % 10
# #     ones_digit = num % 10
# #     if num == hundreds_digit**3 + tens_digit**3 + ones_digit**3:
# #         print(num, end=" ")
# # print()
# #
# #202358234044 吴振博
# # grades = []
# # while True:
# #     grade = input("请输入一个成绩（输入'end'结束）：")
# #     if grade == "end":
# #         break
# #     grades.append(int(grade))
# #
# # excellent = 0
# # good = 0
# # medium = 0
# # passing = 0
# # failing = 0
# #
# # for grade in grades:
# #     if grade >= 90:
# #         excellent += 1
# #     elif grade >= 80:
# #         good += 1
# #     elif grade >= 70:
# #         medium += 1
# #     elif grade >= 60:
# #         passing += 1
# #     else:
# #         failing += 1
# #
# # print(f"优秀人数：{excellent}")
# # print(f"良好人数：{good}")
# # print(f"中等人数：{medium}")
# # print(f"及格人数：{passing}")
# # print(f"不及格人数：{failing}")
# #
# # # 202358234044 吴振博
# # for i in range(1, 10):
# #     for j in range(1, i + 1):
# #         print(f"{j}×{i}={i * j}\t", end="")
# #     print()
# #
# # 202358234044 吴振博
# # for num in range(200, 0, -1):
# #     if num % 17 == 0:
# #         print(num)
# #         break
# #
# #
# # 202358234044 吴振博
# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
# #
# # num = int(input("请输入一个整数："))
# # if is_prime(num):
# #     print(f"{num}是素数。")
# # else:
# #     print(f"{num}不是素数。")
# #
# #
# # 202358234044 吴振博
# # for chicken in range(0, 31):
# #     rabbit = 30 - chicken
# #     if chicken * 2 + rabbit * 4 == 90:
# #         print(f"鸡有{chicken}只，兔有{rabbit}只。")
# #
# #
# # 202358234044 吴振博
# #
# # for i in range(1, 5):
# #     for j in range(1, 5):
# #         for k in range(1, 5):
# #             if i!= j and i!= k and j!= k:
# #                 print(i * 100 + j * 10 + k)
# #
# # # 202358234044 吴振博
# # for num in range(1, 1000):
# #     if num % 4 == 1 and num % 5 == 2 and num % 9 == 7:
# #         print(f"这箱苹果至少有{num}个。")
# #         break
# #
# # principal = float(input("请输入本金："))
# # rate = float(input("请输入收益率："))
# # years = int(input("请输入投资年限："))
# #
# # for _ in range(years):
# #     principal *= (1 + rate)
# #
# # print(f"最终收益为{principal}。")
# #
# #
# # # 202358234044 吴振博
# # n = int(input("请输入 n："))
# # sum_factorial = 0
# # for i in range(1, n + 1):
# #     factorial = 1
# #     for j in range(2, i + 1):
# #         factorial *= j
# #     sum_factorial += factorial
# #
# # print(sum_factorial)
# #
# #
# # 202358234044 吴振博
# def kaprekar(num):
#     iterations = 0
#     while num!= 6174:
#         digits = [int(digit) for digit in str(num)]
#         largest = int(''.join(map(str, sorted(digits, reverse=True))))
#         smallest = int(''.join(map(str, sorted(digits))))
#         num = largest - smallest
#         iterations += 1
#         if iterations > 7:
#             return False
#     return True
#
# num = int(input("请输入一个四位数字："))
# if kaprekar(num):
#     print(f"经过验证，对于数字{num}，6174猜想成立。")
# else:
#     print(f"经过验证，对于数字{num}，6174猜想不成立。")





#202358234044 吴振博
# year = int(input("请输入一个四位整数："))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")


#202358234044 吴振博

# import random
# nums=[random.randint(1,101) for _ in  range(50)]
# for i in range(len(nums) - 1, -1, -1):
#     if nums[i] % 2 != 0:
#         nums.pop(i)
# print("删除所有奇数后的列表:", nums)




#202358234044 吴振博
# import random
# nums = [random.randint(1, 100) for _ in range(20)]
# dnums = sorted(nums[::2], reverse=True)
# nums[::2] =dnums
#
# print("偶数下标降序后的列表:", nums)


#202358234044 吴振博
# num = int(input("请输入小于1000的整数："))
# if num < 1000:
#     f = []
#     d = 2
#     while num > 1:
#         while num % d == 0:
#             f.append(d)
#             num //= d
#         d += 1
#     print(f"{num} 的因式分解为：{' × '.join(map(str, f))}")
# else:
#     print("请输入小于 1000 的整数！")


#202358234044 吴振博
# sum = sum(i for i in range(1, 100, 2))
# print("100 以内所有奇数的和:", sum)


#202358234044 吴振博
# import itertools
#
# digits = '1234'
# a = itertools.permutations(digits)
# primes = set()
# for perm in a:
#     num = int(''.join(perm))
#     if num <= 1:
#         continue
#     if num == 2:
#         primes.add(num)
#         continue
#     if num % 2 == 0:
#         continue
#     is_prime = True
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.add(num)
# print("由1、2、3、4组成的素数有：")
# for prime in sorted(primes):
#     print(prime)

#202358234044 吴振博
for x in range(-5, 25):
    if x < 0:
         print(f"x = {x}, y = {0}")
    elif 0 <= x < 5:
        print(f"x = {x}, y = {x}")
    elif 5 <= x < 10:
         print(f"x = {x}, y = {3 * x - 5}")
    elif 10 <= x < 20:
         print(f"x = {x}, y = {0.5 * x - 2}")
    else:  # 20≤x
        print(f"x = {x}, y = {0}")
