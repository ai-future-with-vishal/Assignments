# 6. Write a program which accept number from user and whether that number is positive, negetive or zero.
# Input : 11                    Output : Positive
# Input : -8                    Output : Negative
# Input : 0                     Output : Zero

def NumCheck(Number):
    if(Number > 0):
        print("Positive")
    elif(Number < 0):
        print("Negative")
    else:
        print("Zero")

def main():
    print("Enter number : ")
    No = int(input())

    NumCheck(No)

if __name__ == "__main__":
    main()


