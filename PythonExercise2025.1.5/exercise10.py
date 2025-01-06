class Student:
    name: str = None
    age: int = None
    gender: int = None
    __id: int = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    

