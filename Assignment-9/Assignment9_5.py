# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5.

def Divisible():
    print("Enter number : ")
    No = int(input())

    if(No % 3 == 0 & No % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

Divisible()