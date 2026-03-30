# 3.Design a python application where multiple threads update and shared variable.
# Use a Lock to avoid race condition
# Each thread should increment the shared counter multiple times
# Display the final value of the counter after all threads complete execution.

import threading
lock = threading.Lock()

counter = 0

def Increment(Thread_name, Times):
    global counter

    for i in range(Times):
        lock.acquire()
        counter = counter + 1
        print(f"{Thread_name} -> counter = {counter}")
        lock.release()


def main():
    global counter

    counter = 0

    print("Thread ID : ",threading.get_ident())

    t1 = threading.Thread(target=Increment, args=("Thread-1", 5),name="Thread-1")
    t2 = threading.Thread(target=Increment, args=("Thread-2", 5),name="Thread-2")
    t3 = threading.Thread(target=Increment, args=("Thread-3", 5),name="Thread-3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\nFinal counter value : ",{counter})
    print(f"Exit from main")

if __name__ == "__main__":
    main()