# 5.Design a Python application that creates two threads names as Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 reverse order.
# Ensure that:
#       Thread2 start execution only after Thread1 has completed.
# Use appropriate thred synchronization.

import threading

def DisplayBySerialOrder():
    for no in range(1,51):
        print("Thread 1 : ",no)

def DisplayByReverseOrder():
    for no in range(50,0,-1):
        print("Thread 2 : ",no)
        
def main():
    print("Thread ID is : ",threading.get_ident())

    t1 = threading.Thread(target=DisplayBySerialOrder)
    t2 = threading.Thread(target=DisplayByReverseOrder)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()