# 2.Design a python application that creates a two threads.
#   Thread 1 should calculate and display the maximum element from an list.
#   Thread 2 should calculate and display the mimimum element from an list.
# This list should be accepted from the user.

import threading

def Max(NumList):
    Max = NumList[0]
    for no in NumList:
        if(Max < no):
            Max = no

    print("Max number is : ",Max)

def Min(NumList):
    Min = NumList[0]
    for no in NumList:
        if(Min > no):
            Min = no

    print("Min number is : ",Min)

def main():
    print("Thread ID : ",threading.get_ident())

    print("Enter zize of list : ")
    No = int(input())

    List = []

    print("Enter list of elements : ")
    for no in range(No):
        value = int(input())
        List.append(value)

    t1 = threading.Thread(target=Max, args=(List,))
    t2 = threading.Thread(target=Min, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()