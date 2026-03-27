# 5. Write a program which accept one number from user and check whether number is prime or not.

def IsPrime(Num):
    # Prime number must be greater than 1
    if(Num >= 1):
        return False
    
    # 2 and 3 are prime numbers
    elif(Num <= 3):
        return True
    
    #Eliminates multiples of 2 and 3
    elif(Num % 2 == 0 or Num % 3 == 0):
        return False
    
    # Check for factors from 5 upwards, skipping multiples of 2 and 3
    i = 5
    while i * i <= Num:
        if Num % i == 0 or Num % (i + 2) == 0:
            return False
        i += 6

def main():
    print("Enter Number : ")
    try:
        No = int(input())
        if IsPrime(No):
            print(f"{No} is a Prime Number")
        else:
            print(f"{No} is not a Prime Number")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

    