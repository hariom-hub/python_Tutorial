# practice set for conditional statements
# question 1
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# num4 = int(input("Enter number 4 : "))
#
# if (num1 > num2 and num1 > num3) and num1 > num4:
#     print("num1 is the greatest number.")
# elif (num2 > num1 and num2 > num3) and num2 > num4:
#     print("num2 is the gretest number.")
# elif (num3 > num1 and num3 > num2) and num3 > num4:
#     print("num3 is the greatest number.")
# else:
#     print("num4 is the greatest number.")
from idlelib.colorizer import prog_group_name_to_tag
from tabnanny import check

# question 2

# marks1 = int(input("Enter the marks : "))
# marks2 = int(input("Enter the marks : "))
# marks3 = int(input("Enter the marks : "))
#
# if (((marks1 + marks2 + marks3) / 300) * 100) >= 33:
#     print("passed")
# else:
#     print("failed")

# question 3
# spam1 = "Makes a lot of money"
# spam2 = "buy now"
# spam3 = "subscribe this"
# spam4 = "click this"
#
# check_spam = input("Enter a sentence : ")
# if check_spam == spam1 :
#     print("this is a spam")
# elif check_spam == spam2 :
#     print("this is a spam")
# elif check_spam == spam3 :
#     print("this is a spam")
# elif check_spam == spam4 :
#     print("this is a spam")
# else:
#     print("not a spam sentence.")

# question 4
# username = input("Enter a username : ")
# if len(username) < 10 :
#     print("less than 10 chars")
# else :
#     print("more than or equal to 10 chars")

# question 5

# li = ["hariom","gaurisha","shreesha","navneet","babita","manju"]
#
# name = input("Enter your name : ")
# if name in li:
#     print("your name is present in the list.")
# else:
#     print("your name is not present in the list.")

# question 6

grade = int(input("Enter the grades : "))

if 90 <= grade <= 100:
    print("Excellent.")
elif 80 <= grade <= 90:
    print("A")
elif 70 <= grade <= 80:
    print("B")
elif 60 <= grade <= 70:
    print("C")
elif 50 <= grade <= 60:
    print("D")
else:
    print("Fail")

# question 7

# post = input("Enter the post details : ")
# name = input("Enter the name : ")
# if name in post :
#     print("post is talking about the name.")
# else:
#     print("post is not talking about the name.")
