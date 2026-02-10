# 8. Write a program which accept number from user and print that number of "*" on screen.
# Input : 5                         Output : *  *   *   *   *

def PrintStar(Number):
    for i in range(Number):
        print("*")

def main():
    print("Enter number : ")
    No = int(input())

    PrintStar(No)

if __name__ == "__main__":
    main()