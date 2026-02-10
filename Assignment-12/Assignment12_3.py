# 3. Write a program which accepts two numbers and prints Addition, Substraction, Division and Multiplication.

def Addition(Value1, Value2):
    return Value1 + Value2

def Substraction(Value1, Value2):
    return Value1 - Value2

def Multiplication(Value1, Value2):
    return Value1 * Value2

def Division(Value1, Value2):
    return Value1 / Value2

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = Addition(No1, No2)
    print("Addition is : ",Ret)

    Ret = Substraction(No1, No2)
    print("Substraction is : ",Ret)

    Ret = Multiplication(No1, No2)
    print("Multiplication is : ",Ret)

    Ret = Division(No1, No2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()