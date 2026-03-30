# 1. Write a Python program to implement a class named Demo with the following specifications:
#       The class should contain two instance variables : no1 and no2.
#       The class should contain one class variable named value.
#       Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
#       Implement two instance methods:
#           Fun() -> displays the value of instance variables no1 and no2.
#           Gun() -> display the values of instance variables no1 and no2.
#       
#       Create two objects of the Demo class as follows:
#       
#       obj1 = Demo(11, 21)
#       obj2 = Demo(51, 101)
#
#       Call the instance methods in the given sequence:
#       
#       obj1.Fun()
#       obj2.Fun()
#       obj1.Gun()
#       obj2.Gun()

class Demo:

    value = 10

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("display the value of instance variable no1 in Fun : ",self.no1)
        print("display the value of instance variable no2 in Fun : ",self.no2)

    def Gun(self):
        print("display the value of instance variable no1 in Gun : ",self.no1)
        print("display the value of instance variable no2 in Gun : ",self.no2)

    print("display the value of class variable is : ",value)
    
def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()