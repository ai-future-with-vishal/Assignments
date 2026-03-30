# 2. Write a python program to implement a class named Circle with the following requirements:
#   The class should contain three instance variables: Radius, Area, and Circumference.
#   The class should contain one class variable named PI, initilzes to 3.14
#   Define a constructor (__init__) that initializes all instance variables to 0.0
#   Implement the following instance methods:
#       Accept() -> accepts the radious of the circle from the user
#       CalculateArea() -> calculates the area of the circle and stores it in the area variable.
#       CalculateCircumference() -> calculate the circumference of the circle ans stores it in the Circumference variable.
#       Display() -> displays the values of Radious, Area, and Cicumference.
#
#   Create multiple objects of the Circle class and invoke all the instance methods for each object.


class Circle:
    
    PI = 3.14

    def __init__(self):
        self.Radious = 0.0
        self.Area = 0.0
        self.Cicumference = 0.0

    def Accept(self):
        self.Radious = float(input("Enter Radious of the circle : "))

    def CalculateArea(self):
        self.area = self.Radious * self.Radious * Circle.PI
    
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.Radious
    
    def Display(self):
        print(f"\n  Radius        : {self.Radious}")
        print(f"  Area          : {self.area:.2f}")
        print(f"  Circumference : {self.circumference:.2f}")

def main():
    obj1 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Circle()
    
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()