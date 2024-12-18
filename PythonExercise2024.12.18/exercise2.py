# 函数说明文档

def add(number1, number2):
    """
    add函数可以需要传递两个参数，然后将两个参数相加并返回
    :param number1:
    :param number2:
    :return: number1 + number2
    """
    return number1 + number2


# python局部变量和全局变量
# 函数中的是局部变量
# 函数外的是全局变量
name = "张三"
print(name)

# 通过global关键字将函数内的变量定义为全局变量
def show():
    global name
    name = "李四"
    print(name)

if __name__ == '__main__':
    show()
    print(name)
