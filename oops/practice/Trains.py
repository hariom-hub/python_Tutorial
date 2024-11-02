class indianTrains:
    def booktickect(self):
        n = int(input("Enter the number of passengers : "))
        passengers = list()
        for x in range(0, n):
            passengers.append(input(f"Enter the name of the passenger {x} : "))

        print(f"passengers for journey : {passengers}")

    def getStaus(self):
        tickets = int(input("Enter the number of tickets you want to book : "))
        print(f"tickets booked = {tickets}")

    def fareInfo(self):
        trains_running = 10
        print(f"number of trains running today is : {trains_running}")


obj = indianTrains()
obj.fareInfo()
