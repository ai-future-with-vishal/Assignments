# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwiae return false.

def DivisibleFive(Number):

    if(Number % 5 == 0):
        return 1
    else:
        return 0
    
def main():
    print("Enter number : ")
    No = int(input())

    Ret = DivisibleFive(No)

    if(Ret == 1):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()