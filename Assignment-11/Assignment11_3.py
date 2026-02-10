# 3. Write a program which accept one number and print Sum of that digit.
# Input : 123
# Output : 6

def SumofDigits():
    print("Enter numbers : ")
    Numbers = int(input())

    Sum = 0
    while Numbers > 0:
        Sum = Sum + (Numbers % 10)
        Numbers //= 10

    print(Sum)

SumofDigits()

        