# 4.Write a program whcih accept N numbers from user and store it into List. Accept one another number from user
# and return frequency of that number from list.
# Input : Number of Elements : 11
# Input Elements : 13   5   45  7   4   56  5   34  2   5   65
# Element to search : 5
# Output : 3

def FrequencyOfNumber(NumList, Ele):

    Count = 0
    for no in NumList:
        if(Ele == no):
            Count = Count + 1

    return Count

def main():
    print("Enter Number of elements : ")
    No = int(input())

    List = []
    print("Enter List of elements : ")
    for i in range(No):
        i = int(input())
        List.append(i)

    print("Enter frequency of number : ")
    Ele = int(input())

    Ret = FrequencyOfNumber(List, Ele)

    print("Frequency of number : ",Ret)

if __name__ == "__main__":
    main()