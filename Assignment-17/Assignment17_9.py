# 9. Write a program which accept number from user and return number of digts that number.
# Input : 3247688           Output : 7

def CountLengthofNumber(Number):
    Ans = len(Number)
    return Ans

def main():
    print("Enter number : ")
    No = list(input())

    Ret = CountLengthofNumber(No)

    print(Ret)

if __name__ == "__main__":
    main()