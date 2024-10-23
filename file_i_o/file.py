# with open("file.txt","w") as file:
#     file.write("hello world")
#     file.write("hello gadhe")
from os import write

from win32comext.shell.demos.IShellLinkDataList import console_props


# with open("file.txt","r") as file:
#     contents = file.read()
#     print(contents)

# with open("hariom.txt","w") as file:
#     file.write("hello hariom.")
#
# with open("hariom.txt","r") as file:
#     data = file.read()
#     print(data)

# with open("hairom.txt","w") as file:
#     file.write("\n gadhe ho tum")

# with open("hariom.txt","w") as hariomfile:
#     hariomfile.write("\n this is another file.")
#     hariomfile.write("\n this is hairom's file.")


# def writeFile():
#     filename = input("Enter file name : ")
#     with open(f"{filename}.java", "w") as newFile:
#         filedata = input("Enter the file data : ")
#         newFile.write(filedata)
#         print(filedata)
#
# writeFile()

# def readfromFile():
#     fileName = input("Enter the file name : ")
#     with open(f"{fileName}.txt", "r") as read_file:
#         data = read_file.read()
#         print(data)
#         read_file.close()
#
#
# readfromFile()
newData = "I am doing well btw how are you?"
mydata = "\n microsoft"
file = open("myfile.txt","a")
file.write(mydata)
file.close()





