# 10. Write a lambda function which accepts three numbers and return largest number.

LargestNum = lambda A, B, C : max(A, B, C)

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    print("Enter thired number : ")
    No3 = int(input())

    Ret = LargestNum(No1, No2, No3)

    print("Largest Number is : ", Ret)

if __name__ == "__main__":
    main()