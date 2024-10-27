words = ["donkey", "mc", "bc", "bsdk"]

for x in range(len(words)):
    if (words[x] == "donkey" or words[x] == "mc") or (words[x] == "bc" or words[x] == "bsdk"):
        words[x] = "####censoredchat"

print(words)