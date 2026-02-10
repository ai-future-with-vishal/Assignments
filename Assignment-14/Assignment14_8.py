# 8. Write a lambda function which accepts two numbers and returns addition of that numbers.

Addition = lambda A, B : A + B

def main():
    print("Enter first Number : ")
    No1 = int(input())

    print("Enter second Number : ")
    No2 = int(input())

    Ret = Addition(No1, No2)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()