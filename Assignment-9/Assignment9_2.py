# 2. Write a program which contains one function ChkGreater() which accepts two numbers and print the greater number.

def ChkGreater():
    print("Enter first number : ")
    No1 = input()

    print("Enter second number : ")
    No2 = input()

    if (No1 > No2):
        print(No1,"is greater")
    else:
        print(No2,"is greater")

ChkGreater()