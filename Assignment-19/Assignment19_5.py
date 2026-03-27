# 5. Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply
# each number by 2. Reduce will return Maximum number from that numbers. (you can also use normal functions isted of lambda functions).

# Enter elements of list = 8
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2,   11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def IsPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def MultiplyByTwo(no):
    return no * 2

def FindMax(a, b):
    if a > b:
        return a
    else:
        return b
    
def main():
    print("Enter size of list : ")
    No = int(input())

    List = []
    print("Enter elements in the list : ")
    for i in range(No):
        Value = int(input())
        List.append(Value)

    FData = list(filter(IsPrime, List))
    print("After filter Data : ",FData)

    MData = list(map(MultiplyByTwo, FData))
    print("After Map Data : ",MData)

    RData = reduce(FindMax, MData)
    print("After Reduce Data : ",RData)


if __name__ == "__main__":
    main()