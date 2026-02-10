# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input : 121
# Output : Palindrome

def Palindrome():
    print("Enter number : ")
    No = int(input())

    Temp = No
    Reverse = 0
    while No > 0:
        Digit = No % 10
        Reverse = Reverse * 10 + Digit
        No //= 10

    if(Temp == Reverse):
        print("Palindrome")
    else:
        print("Not a Palindrome")

Palindrome()