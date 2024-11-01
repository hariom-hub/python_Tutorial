class greet:
    @staticmethod
    def Greet():
        userName = input("Enter your name : ")
        print(f"welcome to the community : {userName}")


obj = greet()
obj.Greet()