# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4  3                Output : 12
# Input : 6  3                Output : 18

Multiplication = lambda A, B : A * B

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Result = Multiplication(Value1, Value2)

    print("Multiplication of number : ",Result)

if __name__ == "__main__":
    main()