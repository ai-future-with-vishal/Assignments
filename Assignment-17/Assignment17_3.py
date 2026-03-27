# 3.Write a program which accept one number from user and return its factorial.print.
# Input : 5
# Output : 120

def Factorial(Number):
    Fact = 1
    for i in range(Number, 1, -1):
        Fact = Fact * i
    
    return Fact

def main():
    print("Enter number : ")
    No = int(input())

    Ret = Factorial(No)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main() 