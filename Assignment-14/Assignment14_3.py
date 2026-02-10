# 3. Write a lambda function which accepts two numbers and retun maximum number.

MaxNumber = lambda A, B : A if A > B else B

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = MaxNumber(No1, No2)

    print("Maximum Number is : ", Ret)

if __name__ == "__main__":
    main()