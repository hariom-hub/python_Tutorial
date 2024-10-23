poem = "\ntwinke twinkle little star, how I wonder how you are"
# print(poem)

# with open("poem.txt", "r") as poemFile:
#     if poemFile.read().__contains__("twinkle"):
#         print("yes twinkle exists")
#     else:
#         print("twinkle doesn't exists")

with open("poem.txt","a") as poemFile:
    poemFile.write(poem)
    poemFile.close()