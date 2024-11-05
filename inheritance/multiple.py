class parent1:
    a = 20

    def Print(self):
        print(self.a)


class parent2:
    b = 30

    def Print_(self):
        print(self.b)


class child(parent1, parent2):

    # using data members using dunder method
    def __init__(self):
        print(self.a)
        print(self.b)

    # using user build function to access data members
    def access(self):
        self.Print()
        self.Print_()


obj = child()
# obj.Print()
# obj.Print_()
