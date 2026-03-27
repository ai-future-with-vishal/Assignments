# 5. Write a program whcih accept N numbers from user and store it into List. Return Addition of all prime numbers from that list.
# main Python file accepts N number from user and pass each number to ChkPrime() function which is part of our user defined model
# named as MarvellousNum. Name of the function from main python file should be ListPrime().

# Input : Number of Elements : 11
# Input Elements : 13   5   45  7   4   56  10  34  2   5 8
# Output : 32(13+5+7+2+5)

import MarvellousNum

def ChkPrime(NumList):
    PrimeList = []
    for no in NumList:
        Is_prime = True
        if no < 2:
            Is_prime = False
            
        for i in range(2, no):
            if no % i == 0:
                    Is_prime = False
                    break
        if Is_prime == True:
                PrimeList.append(no)

    Result = MarvellousNum.Addition(PrimeList)

    return Result

def main():
    print("Enter number of elements : ")
    No = int(input())

    List = []

    print("Input Elements : ")
    for i in range(No):
        i = int(input())
        List.append(i)

    Ret = ChkPrime(List)

    print('Addition of Prime number is : ',Ret)

if __name__ == "__main__":
    main()