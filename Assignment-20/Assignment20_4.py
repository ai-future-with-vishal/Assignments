# 4.Design a Python application that creates three threads named small, capital, and digits.
# All threads should accept a string as a input.
# The small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric Digits.
#       Each thread much also display :
#           Thread ID
#           Thread Name

import threading

def SamllCharactor(Char):
    count = 0
    for ch in Char:
        if ch.islower():
            count = count + 1

    print(f"Thread Id : ",threading.get_ident())
    print(f"Thread name : ",threading.current_thread().name)
    print(f"Count of lowercase charactors : ",count)


def CapitalCharactor(Char):
    count = 0
    for ch in Char:
        if ch.isupper():
            count = count + 1

    print(f"Thread Id : ",threading.get_ident())
    print(f"Thread name : ",threading.current_thread().name)
    print(f"Count of Uppercase charactors : ",count)

def Digits(Char):
    count = 0
    for ch in Char:
        if ch.isdigit():
            count = count + 1

    print(f"Thread Id : ",threading.get_ident())
    print(f"Thread name : ",threading.current_thread().name)
    print(f"Count of digits : ",count)

def main():
    print("Thread Id : ",threading.get_ident())
    print("Main Thread name : ",threading.current_thread().name)

    Ch = input("Enter Sting as a input : ")

    Small = threading.Thread(target=SamllCharactor, args=(Ch,), name="SmallCharactor")

    Capital = threading.Thread(target=CapitalCharactor, args=(Ch,), name="CapitalCharactor")

    Digit = threading.Thread(target=Digits, args=(Ch,), name="Digits")

    Small.start()
    Capital.start()
    Digit.start()

    Small.join()
    Capital.join()
    Digit.join()

    print(f"Exit from main")

if __name__ == "__main__":
    main()