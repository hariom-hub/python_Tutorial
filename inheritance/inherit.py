class company:
    companyName = "microsoft"
    valuation = "3.8 trillion dollars"


class companyData(company):

    def __init__(self,name):
        print(name)
        print(self.companyName)
        print(self.valuation)

    a = 10

class hariom(companyData):
    print(companyData.a)

obj = companyData("hariom")


