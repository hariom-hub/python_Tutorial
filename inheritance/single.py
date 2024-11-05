# single level inheritance
class parent:
    a = 10
    name = "hariom"


class child(parent):
    def __init__(self):
        print(self.a)
        print(self.name)


class hariom:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)


obj = hariom("hariom",20)
