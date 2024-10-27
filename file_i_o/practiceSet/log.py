# with open("log.txt", "r") as logFile:
#     content = logFile.read()
#
# if "python" in content:
#     print("python found")
# else:
#     print("python not found")

with open("log.txt", "r") as logFile:
    lines = logFile.readlines()

lineno = 1

for line in lines:
    if "python" in line:
        print(f"yes python is present in the line number : {lineno}.")
        break
    lineno += 1


else:
    print("python is not found in the file.")
