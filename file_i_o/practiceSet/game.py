import random


def game():
    print("--------Game Started-------------")
    score = random.randint(1, 62)
    # fetch the highscore
    with open("highscore.txt","r") as gamefile:
        highscore = gamefile.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score : {score}")
    if score > highscore:
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score


game()
