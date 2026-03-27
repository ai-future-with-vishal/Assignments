# 4. Write a program which accept one number from user and return addition of its factors.
# Input : 12
# Output : 16 (1+2+3+4+6)

def Factors(Num):
    FactSum = 0
    for i in range(1,Num):
        if(Num % i == 0):
            FactSum = FactSum + i
    
    return FactSum

def main():
    print("Enter number : ")
    No = int(input())

    Ret = Factors(No)

    print("Factors is : ",Ret)

if __name__ == "__main__":
    main()