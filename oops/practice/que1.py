class programmer:
    company = "Microsoft"
    name = input("Enter the employee name : ")
    degree = input("Enter the degree attained : ")
    skills = input("Enter the skills : ")
    exp = input("Enter the working experience : ")

    def __init__(self):
        print("------------Employee details-----------")
        print(self.company)
        print(self.name)
        print(self.degree)
        print(self.skills)
        print(self.exp)


obj = programmer()
