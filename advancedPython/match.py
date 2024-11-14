def checkNum(num):
    match num:
        case 1:
            print("num found")
        case 2:
            print("num not found")
        case _:
            print("invalid num entered.")


checkNum(1)
# match in python is like switch case in java,c/c++ and js
