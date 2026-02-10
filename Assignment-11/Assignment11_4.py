# 4. Write a program which accepts one number and prints revers of that number.
# Input : 123
# Output : 321

def ReverseNumber():
    print("Enter number : ")
    No = int(input())

    Reverse = 0
    while No > 0:
        Digit = No % 10
        Reverse = Reverse * 10 + Digit
        No //= 10

    print(Reverse)

ReverseNumber()