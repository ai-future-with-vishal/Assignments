# 5. Write a lambda function which accept one number retuns TRUE if number is Odd otherwise FALSE.

EvenNumber = lambda A : True if(A % 2 == 1) else False

def main():
    print("Enter Number : ")
    No = int(input())

    Ret = EvenNumber(No)

    if(Ret == True):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()