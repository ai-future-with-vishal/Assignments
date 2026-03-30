# 2.Design a python application that creates two separate threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter
# The EvenFactor Thread should:
#       Identify all even factors of the given number.
#       Calculate and Display the sum of even factors.
# The OddFactor Thred should:
#       Identify all odd factors of the given number.
#       Calculate and Display the sum of odd factors.
# After both thread complete execution, The main thread should display the message:
# "Exit from main"

import threading

def EvenFactor(No):
    sum = 0
    even_factors = []

    for i in range(1,No+1):
        if(No % i == 0 and i % 2 == 0):
            even_factors.append(i)
            sum = sum + i

    print("Even factors is : ",even_factors)
    print("Even factors sum is : ",sum)

def OddFactor(No):
    sum = 0
    Odd_factors = []

    for i in range(1,No+1):
        if(No % i == 1 and i % 2 == 1):
            Odd_factors.append(i)
            sum = sum + i

    print("Odd factors is : ",Odd_factors)
    print("Odd factors sum is : ",sum)

def main():
    No = int(input("Enter number : "))

    print("\nMain Thread ID : ",{threading.get_ident()})
    print(f"Finding factors of : {No}\n")

    t1 = threading.Thread(target=EvenFactor, args=(No,))
    t2 = threading.Thread(target=OddFactor, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from main")

if __name__ == "__main__":
    main()
