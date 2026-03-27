# 2. Write a program whcih accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of Elements : 7
# Input Elements : 13   5   45  7   4   56  34
# Output : 56

def MaximumNum(NumList):
    Max = NumList[0]
    for no in NumList:
        if(Max < no):
            Max = no

    return Max

def main():
    print("Enter Number of Elements : ")
    No = int(input())

    List = []

    for i in range(No):
        List.append(int(input()))

    print("Maximum Number is : ",MaximumNum(List))

if __name__ == "__main__":
    main()