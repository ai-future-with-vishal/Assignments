# 2. Write a program which accept one number and display below pattern.
# Input : 5
# Output :  *    *   *   *   *
#           *    *   *   *   *
#           *    *   *   *   *
#           *    *   *   *   *
#           *    *   *   *   *

def PatternPrinting(Number):
    for i in range(Number):
        for j in range(Number):
            print("*", end=" ")
        print()

def main():
    print("Enter Number : ")
    No = int(input())

    PatternPrinting(No)

if __name__ == "__main__":
    main()
           