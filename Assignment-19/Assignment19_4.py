# 4. Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers.
# List contains the number which are accepted from user. Filter should filter out all such numbers which are even. Map function 
# will calculate its square. Reduce will return addition of all that numbers.

# Enter number of elements in list = 10
# Input List = [5   2   3   4   3   4   1   2   8   10]
# List After filter = [2    4   4   2   8   10]
# List After map = [4   16  16  4   64  100]
# Output of reduce = 204

from functools import reduce

def main():
    print("Enter number of elements in list : ")
    No = int(input())

    List = []
    print("Input List : ")
    for i in range(No):
        Value = int(input())
        List.append(Value)

    FData = list(filter(lambda x : x % 2 == 0, List))
    print("After Filter Data : ",FData)

    MData = list(map(lambda x: x * x, FData))
    print("After Map Data : ",MData)

    RData = reduce(lambda x,y : x + y, MData)
    print("Afte Reduce Data : ",RData)
    
if __name__ == "__main__":
    main()