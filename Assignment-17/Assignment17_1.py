# 1. Create on module named as Arithmetic which contains 4 functions as Add() for Addition, Sun() for Substraction, Mult() for Multiplication
# and Div() for Division. All functions accepts two parameters as number and perform the opration. write on python program which call all the 
# Functions from Arithmetic module by accepting the parameters from user.

class Arithmetic:
    def Add(Value1, Value2):
        return Value1 + Value2
    

    def Sub(Value1, Value2):
        return Value1 - Value2
    

    def Mult(Value1, Value2):
        return Value1 * Value2
    

    def Div(Value1, Value2):
        return Value1 / Value2
    
def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = Arithmetic.Add(No1, No2)

    print("Addition is : ",Ret)

    Ret = Arithmetic.Sub(No1, No2)

    print("Substration is : ", Ret)

    Ret = Arithmetic.Mult(No1, No2)

    print("Multiplication is : ", Ret)

    Ret = Arithmetic.Div(No1, No2)

    print("Division is : ", Ret)

if __name__ == "__main__":
    main()
