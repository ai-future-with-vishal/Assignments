# 4.Design a python application that creates two threads.
#   Thread 1 should compute the sum of elements from a list.
#   Thread 2 should compute the product of elements from the same list.
#   Return the results to the main thread and display them.

import threading

def SumofList(NumList):
    sum = 0
    for no in NumList:
        sum = sum + no

    print("Sum of list is : ",sum)

def ProductOfList(NumList):
    product = 1
    for no in NumList:
        product = product * no
    
    print("Product of list is : ",product)

def main():
    print("Thread Id : ",threading.get_ident())

    print("Enter size of list")
    No = int(input())

    List = []
    print("Enter list of numbers : ")
    for i in range(No):
        value = int(input())
        List.append(value)

    t1 = threading.Thread(target=SumofList, args=(List,))
    t2 = threading.Thread(target=ProductOfList, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Exit from main")

if __name__ == "__main__":
    main()           