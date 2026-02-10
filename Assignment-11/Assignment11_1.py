# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input : 11
# Output : Prime Number

def Prime():
    print("Enter Number : ")
    No = int(input())

    if(No <= 1):
        print("Not a prime number")

    else:
        is_Prime = True
        for i in range(2, No):
            if (No % i == 0):
                is_Prime = False
                break
            
        if is_Prime:
            print("Prime Number") 
        else:
            print("Not a prime number")   

Prime() 