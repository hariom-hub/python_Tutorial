# with open("data.txt", "w") as datafile:
#     datafile.write(" \n this is a file" * 5)

def erase():
    with open("data.txt", "w") as data:
        pass

erase()
