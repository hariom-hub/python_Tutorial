# with open("censor.txt", "w") as censorFile:
#     for x in range(10):
#         censorFile.write("BETICHOD Ammu ")

with open("censor.txt", "r") as censorFile:
    content = censorFile.read()

if "BETICHOD" in content:
    content = content.replace("BETICHOD", "#$@#")

with open("censor.txt", "w") as censorFile:
    censorFile.write(content)
