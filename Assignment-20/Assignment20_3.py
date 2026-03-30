# 3.Design a python application that creates two separate threads named EvenList and OddList.
# Both threads should accept List of integers as a parameter
# The EvenList Thread should:
#       Extract all even elements from the list.
#       Calculate and Display the sum.
# The OddList Thred should:
#       Extract all odd elements from the list.
#       Calculate and Display the sum.
# Thread should run concurently.

import threading

def EvenList(NumList):
    EvenLists = []
    Sum = 0
    for no in NumList:
        if(no % 2 == 0):
            EvenLists.append(no)
            Sum = Sum + no
    
    print("Even List is : ",EvenLists)
    print("Even list of sum is : ",Sum)


def OddList(NumList):
    OddLists = []
    Sum = 0
    for no in NumList:
        if(no % 2 == 1):
            OddLists.append(no)
            Sum = Sum + no
    
    print("Odd List is : ",OddLists)
    print("Odd list of sum is : ",Sum)

def main():
    No = int(input("List of size : "))

    List = []
    for no in range(No):
        Value = int(input())
        List.append(Value)

    t1 = threading.Thread(target=EvenList, args=(List,))
    t2 = threading.Thread(target=OddList, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()