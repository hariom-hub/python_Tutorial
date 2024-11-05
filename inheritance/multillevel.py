class Employee:
    name = "sundar pichai"

    # def printname(self):
    #     print(self.name)
    def __init__(self):
        print(self.name)


class manager(Employee):
    name_ = "satya nadella"

    def __init__(self):
        super().__init__()
        print(self.name_)
    # def printname_(self):
    #     print(self.name)


class lead(manager):
    # def getData(self):
    #     self.printname()
    #     self.printname_()
    def __init__(self):
        super().__init__()


obj = lead()
