# 1.Design a Python application that creates two threads named as Prime and NonPrime.
#   Both threads should accept a list of integers
#   The Prime thread should display all primes from the list.
#   The NonPrime thread should display all non-prime numbers from the list.

import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Prime(NumList):
    PrimeList = []
    for no in NumList:
        if is_prime(no):
            PrimeList.append(no)

    print(f"Display all Prime : ",PrimeList)

def NonPrime(NumList):
    NonPrimeList = []
    for no in NumList:
        if not is_prime(no):
            NonPrimeList.append(no)

    print("Display all Non Prime : ",NonPrimeList)

def main():
    print("Thread ID : ",threading.get_ident())

    No = int(input("Enter size of list : "))

    List = []

    print("Enter list of numbers : ")
    for no in range(No):
        value = int(input())
        List.append(value)

    t1 = threading.Thread(target=Prime, args=(List,))
    t2 = threading.Thread(target=NonPrime, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Exit from main")

if __name__ == "__main__":
    main()