
with open("poem.txt", "r") as poemFile:
    data = poemFile.read()
    if data.__contains__("twinkle"):
        print("yes twinkle found")
    else:
        print("twinkle not found.")
