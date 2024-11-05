class hariom:
    a = 20
    # @classmethod is bound to the class not to the object of the class
    @classmethod
    def show(cls):
        print(cls.a)

    def __init__(self):
        print(self.a)

obj = hariom()
obj.a = 30
obj.show()
