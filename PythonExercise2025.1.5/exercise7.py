# python面向对象
class Student:
    name = None
    age = None
    gender = None

    # 构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 方法参数列表中必须有self，相当于this关键字，但是在调用方法时，self可以忽略
    def say_hi(self, msg):
        print(f"hi，大家好，我是{self.name}, {msg}")

if __name__ == '__main__':
    for i in range(5):
        name = input("请输入姓名")
        age = int(input("请输入年龄"))
        gender = input("请输入性别")
        student = Student(name, age, gender)
        msg = input("请输入想要说的话")
        student.say_hi(msg)