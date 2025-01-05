# 函数多返回值
# 函数可以有多个返回值
# 按照返回值的顺序，对应顺序用多个变量接收即可，顺序必须相同!

def test_return():
    return 1, 2


if __name__ == '__main__':
    x, y = test_return()
    print(f"x = {x}  y = {y}")
