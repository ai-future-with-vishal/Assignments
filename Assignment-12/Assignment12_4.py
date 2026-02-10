# 4. Write a program which accepts one number and print that many numbers starting from 1.

def FunNumber(Number):
    for i in range(1, Number+1):
        print(i)

def main():
    print("Enter number : ")
    No = int(input())

    FunNumber(No)

if __name__== "__main__":
    main()