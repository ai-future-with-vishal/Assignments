# 10. Write a program whcih accept number from user and return addition of digit in that number.

def AdditionOfDigits(Num):
    Sum = 0
    while Num > 0:
        Digit = Num % 10
        Sum = Sum + Digit
        Num //= 10

    return Sum 
        
def main():
    print("Enter Number")
    No = int(input())

    Ret = AdditionOfDigits(No)

    print("Addition of Number Count is : ",Ret)

if __name__ == "__main__":
    main()

