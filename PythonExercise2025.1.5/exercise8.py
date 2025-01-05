# 类的魔术方法
# 个人理解为Java中Object类中的方法

class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # __str__魔术方法
    # 个人理解为Java中的toString方法
    def __str__(self):
        return f"当前学生为{self.name}，性别是{self.gender}，年龄是{self.gender}"

    # __lt__魔术方法
    # 个人理解为运算符重载
    # 根据类对象中的某属性自定义比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    # 和lt类似，只是多了＝的判断
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    # 和equals类似
    def __eq__(self, other):
        return self.name == other.name
