# 1. Write a program which accepts one number and prints multiplication table of that number.

def Multiplication():
    print("Enter number : ")
    No = int(input())

    for i in range(1,11):
        Num = No
        Num = Num * i
        print(Num)

Multiplication()