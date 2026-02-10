# 3. Write a program which accept one number and checks whether it is perfect number or not.

def PerfectNumber(Number):
    Sum = 0
    if(Number <= 0):
        print("Not a Perfect Number")
    else:
        for i in range(1,Number):
            if(Number % i == 0):
                Sum = Sum + i

    return Sum

def main():
    print("Enter number : ")
    No = int(input())

    Temp = No
    Ret = PerfectNumber(No)

    if(Temp == Ret):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
    
if __name__ == "__main__":
    main()