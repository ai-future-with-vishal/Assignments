# 2. Write a program which accepts one number and prints Sum of first N Natural numbers.
# Input : 5
# Output : 15

def SumOfNaturalNum():
    print("Enter Number : ")
    No = int(input())

    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i
    
    print(Sum)

SumOfNaturalNum()
