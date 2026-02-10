# 5. Write a program which accepts one number and print many numbers starting from 1 in reverse order.

def ReverseNumber(No):
    for i in range(No, 0, -1):
        print(i)

def main():
    print("Enter number : ")
    No = int(input())

    ReverseNumber(No)

if __name__ == "__main__":
    main()