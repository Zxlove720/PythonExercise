# 202358234044 吴振博
# 1. 编写程序，从键盘输入一个字符串（用逗号分割的若干个整数），删除重复的字符，然后按照字符顺序从小到大顺序输出。
def task1():
    input_str = input("请输入用逗号分割的若干个整数: ")
    num_list = input_str.split(',')
    unique_list = sorted(list(set(num_list)))
    print(','.join(unique_list))


# 202358234044 吴振博
# 2. 编写程序，使用给定的整数 n，生成一个包含 (i, i*i) 的字典，该字典包含 1 到 n 之间的整数(两者都包含)。
def task2():
    result_dict = {}
    n = int(input("请输入整数 n: "))
    for i in range(1, n + 1):
        result_dict[i] = i * i
    print(result_dict)

# 202358234044 吴振博
# 3. 编写程序，用户输入若干整数，试找出其中的最大数和最小数。
def task3():
    input_str = input("请输入若干整数，用空格分隔: ")
    num_list = list(map(int, input_str.split()))
    if num_list:
        max_num = max(num_list)
        min_num = min(num_list)
        print(f"最大数: {max_num}, 最小数: {min_num}")
    else:
        print("未输入有效数字")


# 202358234044 吴振博
# 4. 输入一个字符串，统计每个字符出现的次数。
def task4():
    input_str = input("请输入一个字符串: ")
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)


# 202358234044 吴振博
# 5. 编写程序，给定不超过 10 的正整数 a，给定正整数 n,n 是偶数,6<=n<=16，求 aa+aaaa+aaaaaa+⋯+aa⋯a（n 个 a）之和。
def task5():
    a = int(input("请输入不超过 10 的正整数 a: "))
    n = int(input("请输入满足 6<=n<=16 的偶数 n: "))
    if 0 < a <= 10 and 6 <= n <= 16 and n % 2 == 0:
        total_sum = 0
        num_str = str(a)
        for i in range(2, n + 1, 2):
            num = int(num_str * i)
            total_sum += num
        print(total_sum)
    else:
        print("输入不符合要求")


# 202358234044 吴振博
# 6. 编写程序，生成一个长度为 10，元素值大于 10 小于 100 的整数列表，求其中偶数和奇数的个数。
def task6():
    import random
    num_list = [random.randint(11, 99) for _ in range(10)]
    print("生成的列表:", num_list)
    even_count = 0
    odd_count = 0
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"偶数个数: {even_count}, 奇数个数: {odd_count}")


# 202358234044 吴振博
# 7. 编写程序，输入的若干个整数，通过 s 求这些整数的绝对值之和。
def task7():
    input_str = input("请输入若干整数，用空格分隔: ")
    my_list = input_str.split(" ")
    count = 0
    for e in my_list:
        count += abs(int(e))
    print(count)



# 202358234044 吴振博
# 8. 编写程序，通过 s 求多位整数各位数字之和。
def task8():
    num = int(input("请输入一个多位整数: "))
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    print(f"各位数字之和: {digit_sum}")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    n = 0
    z = 0
    while z <= 2020:
        n += 1
        z += n
    print("n={0}".format(n))