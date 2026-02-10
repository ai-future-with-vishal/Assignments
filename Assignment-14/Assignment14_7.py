# 7. Write a lambda function which accept one number and return True if divisible by 5.

Divisible = lambda A : True if(A % 5 == 0) else False

def main():
    print("Enter number : ")
    No = int(input())

    Ret = Divisible(No)

    print(Ret)

if __name__ == "__main__":
    main()