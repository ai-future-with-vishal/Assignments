# 3. Write a python program to implement a class named Arithmetic with the following characteristics:
#   The class should contain two instance variables: value1 and value2
#   Define a constructor (__init__) that initilizes all instance variables to 0.
#   Implement the following instance methods:
#           Accept() -> accepts values for value1 and value2 from the user.
#           Addition() -> returns the addition of value1 and value2.
#           Substraction() -> returns the substraction of value1 and value2.
#           Multiplication() -> returns the multiplication of value1 and value2.
#           Division() -> returns the division of value1 and value2(handle division by zero properly).
#
#   Create multiple objests of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter value1 : "))
        self.value2 = int(input("Enter value2 : "))

    def Addition(self):
        self.add = self.value1 + self.value2
        print("Addition is : ",self.add)

    def Substraction(self):
        self.sub = self.value1 - self.value2
        print("Substraction is : ",self.sub)

    def Multiplication(self):
        self.Multi = self.value1 * self.value2
        print("Multiplication is : ",self.Multi)

    def Division(self):
        if(self.value1 == 0 or self.value2 == 0):
            return
        else:
            self.Div = self.value1 / self.value2
            print("Division is : ",self.Div)

def main():
    obj1 = Arithmetic()

    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()

if __name__ == "__main__":
    main()