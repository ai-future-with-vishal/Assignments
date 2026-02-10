# 2. Write a program which accepts Redius of a circle and print Area of Circle.

def AreaOFCircle(R, PI):
    Area = PI * R * R
    return Area

def main():
    print("Enter Radius : ")
    Redius = float(input())

    PI = 3.14159

    Area = AreaOFCircle(Redius, PI)

    print("Area of Circle : ",Area)

if __name__ == "__main__":
    main()