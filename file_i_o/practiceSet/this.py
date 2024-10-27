# with open("this.txt","w") as thisfile:
#     thisfile.write("hello world")

# with open("this.txt", "r") as thisfile, open("thiscopy.txt", "w") as copyfile:
#     copyfile.write(thisfile.read())

# with open("hariom.txt","w") as hariom:
#     hariom.write("hello, I am hariom.")

# with open("hariom.txt","r") as hariom, open("ayush.txt","w") as ayush:
#     ayush.write(hariom.read() + "hello I am ayush")

with open("hariom.txt", "r") as hariom, open("ayush.txt", "r") as ayush:
    hariomcontent = hariom.readlines()
    ayushcontent = ayush.readlines()
    if hariomcontent == ayushcontent:
        print("yes the contents of files ayush and hariom are equal.")
    else:
        print("no the contents of files ayush and hariom are not equal.")
