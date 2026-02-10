# 1. Write a lambda function which accept one number and returns square of that number.

Square = lambda A : A * A

def main():
    print("Enter number : ")
    No = int(input())

    Ret = Square(No)
    print(Ret)

if __name__ == "__main__":
    main()