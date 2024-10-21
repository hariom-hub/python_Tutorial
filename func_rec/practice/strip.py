def rem(l, word):
    for item in l:
        if item == word:
            print("word found")
            l.remove(item)
            return l
    print("word not found.")



l = ["hariom", "gaurisha", "shreesha", "gadha"]
word = input("Enter a word : ")
print(rem(l, word))
