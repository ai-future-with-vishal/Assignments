# 3. Write a program which accepts one number and prints factorial of that number.
# Input : 5
# Output : 120

def Factorial():
    print("Enter Number : ")
    No = int(input())

    Fact = 1
    while No:
        Fact = Fact * No
        No = No - 1

    print(Fact)
    
Factorial()