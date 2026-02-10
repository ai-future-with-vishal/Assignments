# 9. Write a lambda function which accepts two numbers and returns multiplication.

Multiplication = lambda A, B : A * B

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    NO2 = int(input())

    Ret = Multiplication(No1, NO2)

    print("Multiplication is : ", Ret)

if __name__ == "__main__":
    main()
