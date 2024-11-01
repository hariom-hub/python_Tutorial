class employee:
    name = "hariom"
    language = "English"
    age = 20

    def printName(self):
        print(f"name = {self.name}", f"age = {self.age}", f"language = {self.language}")

    @staticmethod
    def greet():
        print("hello, good morning.")


obj = employee()
obj.greet()
obj.printName()
