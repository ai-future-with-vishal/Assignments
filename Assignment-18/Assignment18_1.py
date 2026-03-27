# 1. Write a program which accept N number from user and store it into List. Return addition of all elements from that list.
# Input : Number of elements : 6
# Input Elemelts : 13   5   45  7   4   56
# Output : 130

def AdditionOflist(ListofNum):
    Sum = 0
    for i in range(len(ListofNum)):
        Sum = Sum + ListofNum[i]
    return Sum

def main():
    print("Number of Elements : ")
    No = int(input())

    print("List of Elements : ")
    NumList = []
    for i in range(No):
        NumList.append(int(input()))

    print("Addition of list of number : ",AdditionOflist(NumList))

if __name__ == "__main__":
    main()