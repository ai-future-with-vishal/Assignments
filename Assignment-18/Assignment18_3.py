# 3. Write a program whcih accept N numbers from user and store it into List. Return Minimum number from that List.
# Input : Number of Elements : 7
# Input Elements : 13   5   45  7   4   56  34
# Output : 56

def MinimumNumber(NumList):
    Min = NumList[0]

    for no in NumList:
        if(Min > no):
            Min = no
    
    return Min

def main():
    print("Number of elements : ")
    No = int(input())

    List = []
    print("Enter elements : ")
    for i in range(No):
        i = int(input())
        List.append(i)

    Ret = MinimumNumber(List)

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()