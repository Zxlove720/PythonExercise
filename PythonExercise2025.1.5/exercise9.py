# 封装
class Phone:
    # 在属性或方法前面使用 _使其变为私有属性或者私有方法，类似private
    id = None

    def __init__(self, name, gender, id):
        self.name = name
        self.gender = gender
        self.id = id

    def __show_id(self):
        print(self.id)

phone = Phone("1", "1", "1")
print(phone.id)
phone.__show_id()
