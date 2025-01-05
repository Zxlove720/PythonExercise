# 异常
# 读取不存在的文件，出现异常
# with open("C:/abc.txt", "r", encoding="UTF-8") as f:
#     print(f)

# 异常处理
# try:
#     f = open("C:/abc.txt", "r", encoding="UTF-8")
# except FileNotFoundError as e:
#     print(e)


# 捕获多个异常
try:
    a = 1 / 0
    f = open("C:/abc.txt", "r", encoding="UTF-8")
except (ZeroDivisionError, FileNotFoundError) as e:
    print(e)

# 捕获全部异常，和Java一样，顶级异常Exception类
try:
    print(name)
    a = 1/0
    f = open("C:/abc.txt", "r", encoding="UTF-8")
except Exception as e:
    print(e)

print("___________________________________")
# else，是没有异常时进入的分支，finally是无论如何都要进入的分支
# finally可以用于资源释放
try:
    print("hello")
except Exception as e:
    print(e)
else:
    print("没有异常")
finally:
    print("无论如何都要执行")