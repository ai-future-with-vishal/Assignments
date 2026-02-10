# 3. Write a program which contains named as Add(). which accepts two numbers from user and return addition of that two number.
# Input : 11 5
# Output : 16

def Add(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = Add(No1, No2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()