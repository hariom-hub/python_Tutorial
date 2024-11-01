class indianTrains:
    def booktickect(self):
        n = int(input("Enter the number of passengers : "))
        passengers = list()
        for x in range(n):
            passengers[x] = input(f"enter the name of the person {x} : ")

        print(passengers)

    def getStaus(self):
        tickets = int(input("Enter the number of tickets you want to book : "))
        print(f"tickets booked = {tickets}")

    def fareInfo(self):
        trains_running = 10
        print(f"number of trains running today is : {trains_running}")


obj = indianTrains()
obj.booktickect()