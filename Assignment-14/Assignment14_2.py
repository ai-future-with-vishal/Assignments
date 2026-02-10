# 2. Write a lambda function which accepts one number from user and prints cube of that number.

Cube = lambda A : A * A * A

def main():
    print("Enter Number : ")
    No = int(input())

    Ret = Cube(No)

    print(Ret)

if __name__ == "__main__":
    main()