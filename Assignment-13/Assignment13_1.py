# 1. Write a program which accepts length and width of rectangle and prints area.

def AreaOfRectangle(Ln, Wd):
    Area = Ln * Wd
    return Area

def main():
    print("Enter length : ")
    Length = float(input())

    print("Enter width : ")
    Width = float(input())

    Area = AreaOfRectangle(Length, Width)

    print(Area)

if __name__ == "__main__":
    main()
