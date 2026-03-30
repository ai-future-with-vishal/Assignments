# 1. Design a python application that creates two separate threads named Even and Odd.
# The Even Thread should display the first 10 even numbers.
# The Odd Thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution

import threading

def even_numbers():
    print("Even thread started")
    for i in range(2,21):
        if(i % 2 == 0):
            print("Even number : ",i)

def odd_numbers():
    print("Odd thread started")
    for i in range(21):
        if(i % 2 == 1):
            print("Odd number : ",i)
                
def main():
    
    print("Threds successfully created : ",threading.get_ident())

    t1 = threading.Thread(target=even_numbers)
    t2 = threading.Thread(target=odd_numbers)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()